from tkinter import *
from time import strftime
import datetime as dt
import numpy as np
import cv2
import matplotlib
from matplotlib import pyplot as plt
from PIL import Image, ImageTk
from tkinter import filedialog
Lapy = Tk()
Lapy.title("Lapy")
Lapy.geometry("800x492+0+0")
Lapy.configure(bg="lightblue")
bgimg = Image.open(r'C:\Users\Saeem\Downloads\LapyWallpaper.jpg')
photo9 = ImageTk.PhotoImage(bgimg)
photo9_label = Label(Lapy, image=photo9)
photo9_label.place(x=0, y=0)
frame1 = Frame(Lapy, width=804, height=40, bg="black")
frame1.place(x=0, y=452)
def time1():
        string=strftime('%H:%M %p')
        lbl_time.config(text=string)
        lbl_time.after(1000,time1)
def date1():
        date=dt.datetime.now()
        lbl_date.config(text=f"{date:%d-%m-%Y}")
lbl_time=Label(Lapy,font=("Arial",8,"bold"),bg="black",fg="white")
lbl_time.place(x=720,y=454)
lbl_date=Label(Lapy,font=("Arial",8,"bold"),bg="black",fg="white")
lbl_date.place(x=714,y=469)
time1()
date1()
def PE():
    pe = Toplevel(Lapy)
    pe.title("LaPicEditor")
    pe.geometry("550x500+970+1")
    pe.configure(bg="grey")    
    result_label = Label(pe, width=45, height=10, text="", font=("Arial", 10))
    result_label.place(x=40, y=280)
    global img_label 
    img_label = None  
    def openfile():  
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg")])
        if file_path:
            img = Image.open(file_path)
            img.thumbnail((400, 400))
            photo = ImageTk.PhotoImage(img)
            
            global img_label
            if img_label:
                img_label.destroy()

            img_label = Label(pe, image=photo)
            img_label.image = photo
            img_label.place(x=120, y=50)
            
            global img0
            img0 = img
            i1= np.array(img0)           
            result_label.config(text=f"{i1[:10]}")
    
    def clear_image():
        global img_label
        if img_label:
            img_label.destroy()
            img_label = None 
            result_label.config(text="")  
    global img_label1,img_label2
    img_label1=None
    img_label2=None
    def open_file():  # Function for performing image addition, subtraction, and multiplication
        file_path1 = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg")])
        file_path2 = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg")])
    
        if file_path1 and file_path2:
           img1 = Image.open(file_path1)
           img2 = Image.open(file_path2)
        
           img1.thumbnail((150, 150)) 
           img2.thumbnail((150, 150))
        
           photo1 = ImageTk.PhotoImage(img1)
           photo2 = ImageTk.PhotoImage(img2)
        
           global img_label1, img_label2
           if img_label1:
               img_label1.destroy() 
           if img_label2:
               img_label2.destroy()
        
           img_label1 = Label(pe, image=photo1)
           img_label2 = Label(pe, image=photo2)
        
           img_label1.image = photo1 
           img_label2.image = photo2
        
           img_label1.place(x=40, y=100)
           img_label2.place(x=250, y=100)
           global img_path1,img_path2
           img_path1=file_path1
           img_path2=file_path2
    def clear_images():
      global img_label1, img_label2
      if img_label1:
          img_label1.destroy()  
          img_label1 = None
      if img_label2:
          img_label2.destroy()  
          img_label2 = None
    def addimg():
            img11=cv2.imread(img_path1)
            img12=cv2.imread(img_path2)
            height,width,color_scale=img11.shape
            dim=(width,height)
            img12=cv2.resize(img12,dim,interpolation=cv2.INTER_AREA)
            result_label.config(text=f"Original dimension of image1:{img11.shape}\n image2:{img12.shape}")
            add_img=cv2.add(img11,img12)
            titles=[ 'image1','image2','added image']
            images=[img11,img12,add_img]
            for i in range(3):
                   plt.subplot(1,3,i+1),plt.imshow(images[i])
                   plt.title(titles[i])
                   plt.xticks([]),plt.yticks([])
            plt.show()
    def subimg():
            img21=cv2.imread(img_path1)
            img22=cv2.imread(img_path2)
            height,width,color_scale=img21.shape
            dim=(width,height)
            img22=cv2.resize(img22,dim,interpolation=cv2.INTER_AREA)
            result_label.config(text=f"Original dimension of image1:{img21.shape}\n image2:{img22.shape}")
            sub_img=cv2.subtract(img21,img22)
            titles=[ 'image1','image2','subtracted image']
            images=[img21,img22,sub_img]
            for i in range(3):
                   plt.subplot(1,3,i+1),plt.imshow(images[i])
                   plt.title(titles[i])
                   plt.xticks([]),plt.yticks([])
            plt.show()
    def mulimg():
            img31=cv2.imread(img_path1)
            img32=cv2.imread(img_path2)
            height,width,color_scale=img31.shape
            dim=(width,height)
            img32=cv2.resize(img32,dim,interpolation=cv2.INTER_AREA)
            result_label.config(text=f"Original dimension of image1:{img31.shape}\n image2:{img32.shape}")
            mul_img=cv2.multiply(img31,img32)
            titles=[ 'image1','image2','multiplied image']
            images=[img31,img32,mul_img]
            for i in range(3):
                   plt.subplot(1,3,i+1),plt.imshow(images[i])
                   plt.title(titles[i])
                   plt.xticks([]),plt.yticks([])
            plt.show()     
    frame2=Frame(pe,width=150,height=1000,bg="yellow").place(x=450,y=0)
    button=Button(pe,text="📤",font=("Arial",18),command=openfile).place(x=465,y=60)
    clear_button = Button(pe, text="🗑",font=("Arial",18), command=clear_image).place(x=465, y=120)
    button1= Button(pe, text="📤", font=("Arial",18), command=open_file).place(x=465, y=200)
    button2=Button(pe,text="➕",font=("Arial",18),command=addimg).place(x=465,y=250)
    button3=Button(pe,text="➖",font=("Arial",18),command=subimg).place(x=465,y=300)
    button4=Button(pe,text="✖️",font=("Arial",18),command=mulimg).place(x=465,y=350)
    clear_button = Button(pe, text="🗑",font=("Arial",18), command=clear_images).place(x=465,y=410)
    LapicClose=Button(pe,text="X",height=2,width=8,font=("Arial",8,"bold"),bg="red",fg="white",command=pe.destroy).place(x=465,y=10)
def Calc():
    ce = Toplevel(Lapy)
    ce.title("Calc")
    ce.geometry("400x400+1000+1")
    ce.configure(bg="grey")
    frame3=Frame(ce,width=250,height=325,bg="lightgrey").place(x=75,y=30)
    num1_entry = Entry(ce,width=35)
    num1_entry.place(x=90, y=40)
    num2_entry = Entry(ce,width=35)
    num2_entry.place(x=90, y=70)
    result_label = Label(ce,width=26, text="", font=("Arial", 10))
    result_label.place(x=90, y=103)
    def add():
        num1_str = num1_entry.get()  
        num2_str = num2_entry.get()
        try:
            if 'j' in num1_str or 'j' in num2_str:  
                num1 = complex(num1_str)
                num2 = complex(num2_str)
            else:
                num1 = float(num1_str) if '.' in num1_str else int(num1_str)
                num2 = float(num2_str) if '.' in num2_str else int(num2_str) 
            results = (f"{num1 + num2}")
            result_label.config(text=results) 
        except ValueError:
            result_label.config(text="Invalid input! ")
    def sub():
       num1_str = num1_entry.get()
       num2_str = num2_entry.get()
       try:
        if 'j' in num1_str or 'j' in num2_str:
            num1 = complex(num1_str)
            num2 = complex(num2_str)
        else:
            num1 = float(num1_str) if '.' in num1_str else int(num1_str)
            num2 = float(num2_str) if '.' in num2_str else int(num2_str)
        results = f"{num1 - num2}"
        result_label.config(text=results)
       except ValueError:
        result_label.config(text="Invalid Input!")
    def mul():
       num1_str = num1_entry.get()
       num2_str = num2_entry.get()
       try:
        if 'j' in num1_str or 'j' in num2_str:
            num1 = complex(num1_str)
            num2 = complex(num2_str)
        else:  
            num1 = float(num1_str) if '.' in num1_str else int(num1_str)
            num2 = float(num2_str) if '.' in num2_str else int(num2_str)
        results = f"{num1 * num2}"
        result_label.config(text=results)
       except ValueError:
        result_label.config(text="Invalid Input!")
    def div():
        num1_str = num1_entry.get()
        num2_str = num2_entry.get()
        try:
             if 'j' in num1_str or 'j' in num2_str: 
                num1 = complex(num1_str)
                num2 = complex(num2_str)
             else:
                num1 = float(num1_str) if '.' in num1_str else int(num1_str)
                num2 = float(num2_str) if '.' in num2_str else int(num2_str)        
             result = f"{num1 / num2}"
             result_label.config(text=result)
        except ValueError:
             result_label.config(text="Invalid Input!")
        except ZeroDivisionError:
             result_label.config(text="Cannot divide by zero!")
    def mod():
        num1_str=num1_entry.get()
        num2_str=num2_entry.get()
        try:
                num1=float(num1_str) if '.' in num1_str else int(num1_str)
                num2=float(num2_str) if '.' in num2_str else int(num2_str)
                results=(f"{num1%num2}")
                result_label.config(text=results)
        except ValueError:
            result_label.config(text="Invalid input!")
            if 'j' in num1_str or 'j' in num2_str:
                result_label.config(text="Not applicable for complex!")
    def conjugate():
        num1_str = num1_entry.get()
        num2_str = num2_entry.get()
        results = ""  # Assign a default value to results
        try:
             if 'j' in num1_str and not 'j' in num2_str:
                num1 = complex(num1_str)
                results = f"Conjugate of first number: {num1.conjugate()}"
             elif 'j' in num2_str and not 'j' in num1_str:
                num2 = complex(num2_str)
                results = f"Conjugate of second number: {num2.conjugate()}"
             elif 'j' in num1_str and 'j' in num2_str:
                  result_label.config(text="Enter only one complex number.")
                  return
             else:
                  results = "Only applicable for complex numbers."  # Handle non-complex numbers
        except ValueError:
                 results = "Invalid Input!"
        result_label.config(text=results)  # Now results will always have a value
    button23 = Button(ce, text="+", width=5, height=5, font=("Arial", 10), command=add).place(x=265,y=150)
    button24= Button(ce,text="-",width=5,height=2,font=("Arial",10),command=sub).place(x=145,y=150)
    button25= Button(ce,text="*",width=5,height=2,font=("Arial",10),command=mul).place(x=205,y=150)
    button26= Button(ce,text="/",width=5,height=2,font=("Arial",10),command=div).place(x=85,y=200)
    button27= Button(ce,text="%",width=5,height=2,font=("Arial",10),command=mod).place(x=85,y=150)
    button28 = Button(ce,text="con",width=5,height=2,font=("Arial",10),command=conjugate).place(x=145,y=200)
    ClClose=Button(ce,text="X",width=5,height=2,font=("Arial",10,"bold"),bg="red",fg="white",command=ce.destroy).place(x=205,y=200)
def Clock():
    clock=Toplevel(Lapy)
    clock.title("Clock")
    clock.geometry("500x300+805+1")
    clock.config(bg="black")
    def time():
        string=strftime('%H:%M:%S %p')
        lbl.config(text=string)
        lbl.after(1000,time)
    lbl=Label(clock,font=("Arial",40,"bold"),bg="black",fg="white")
    lbl.place(x=90,y=100)
    time()
    def date():
        date=dt.datetime.now()
        lbl=Label(clock,text=f"{date:%A , %B %d , %Y}",font=("Arial",20,"bold"),bg="black",fg="white")
        lbl.place(x=40,y=175)
    date()
    Clockclose=Button(clock,text="X",width=5,height=2,font=("Arial",10,"bold"),bg="red",fg="white",command=clock.destroy).place(x=205,y=40)
def FM():
    fm= Toplevel(Lapy)
    fm.title("file manager")
    fm.geometry("300x350+805+1")
def store():
        store=TopLevel(Lapy)
        store.title("LaStore")
        storegeometry("300x350+805+1")
def Book():
    book= Toplevel(Lapy)
    book.title("Book")
    book.geometry("300x350+805+1")
    bgimg=Image.open(r'C:\Users\Saeem\Downloads\library (2).jpg')
    photo6=ImageTk.PhotoImage(bgimg)
    photo6_label=Label(book, image=photo6).place(x=0,y=0)
    book.photo6=photo6
    booklbl=Label(book,text="Contents",bg="black",fg="white",font=("Arial",20,"bold")).place(x=70,y=2)
    lbl1=Label(book,text="📕 LaPY",bg="black",fg="white",font=("Arial",20,"bold")).place(x=5,y=65)
    lbl2=Label(book,text="📕 LaPicEditor",bg="black",fg="white",font=("Arial",20,"bold")).place(x=5,y=125)
    lbl3=Label(book,text="📕 Calc",bg="black",fg="white",font=("Arial",20,"bold")).place(x=5,y=185)
    lbl4=Label(book,text="📕 Clock",bg="black",fg="white",font=("Arial",20,"bold")).place(x=5,y=245)
    lbl6=Label(book,text="📕 Reference",bg="black",fg="white",font=("Arial",20,"bold")).place(x=5,y=305)
    bookClose=Button(book,text="X",width=5,height=1,font=("Arial",10,"bold"),bg="red",fg="white",command=book.destroy).place(x=230,y=10)
    def LaPY():
        la = Toplevel(book)
        la.title("About LaPY")
        la.geometry("390x350+1110+1")
        la.config(bg="black")
        LaPYlbl = Label(la, text="LaPY", font=("Arial", 20, "bold"),bg="black",fg="white").place(x=120, y=8)
        info_text = (
           "LaPY is a unique operating system that merges\n"
           "the power of Linear Algebra and Python to deliver\n"
           "a flexible and powerful computational environment.\n\n"
           "It offers the following key components:\n"
           "1. LaPicEditor\n"
           "2. Calculator\n"
           "3. Clock\n\n"
           "It supports various functionalities such as\n"
           "image editing,basic arithmetic, and time\n"
           "management.\n\n"
           "Made by Kapadi Mohammad Saif"
            )
        info_label = Label(la, text=info_text, font=("Arial", 11,"bold"),bg="black",fg="white", justify=LEFT).place(x=10, y=60)
        LaPYClose=Button(la,text="X",width=5,height=1,font=("Arial",10,"bold"),bg="red",fg="white",command=la.destroy).place(x=320,y=13)
    button = Button(book, text="Open",width=5, height=1, font=("Arial", 10,"bold"), command=LaPY).place(x=230, y=70)
    def LaPicEditor():
            lap=Toplevel(book)
            lap.title("About LaPicEditor")
            lap.geometry("390x350+1110+1")
            lap.config(bg="black")
            LaPiclbl=Label(lap,text="LaPicEditor",bg="black",fg="white",font=("Arial",20,"bold")).place(x=80,y=8)
            info_text = (
           "A dynamic image editor enhanced with linear\n"
           "algebra capabalities.\n"
           "Facilitates advanced pixel-level image\n"
           "manipulations using mathematical operations.\n\n"
           "It offers the following functionalities:\n"
           "1. get(): Retrive specific image data for detailed\n"
           "analysing or editing.\n"
           "2. add(): Adds one image layer over another.\n"
           "3. mul(): Multiplication of two images for\n"
           "pixel-level transformations and effects.\n"
           "4. sub(): Subtraction of one image layer with other.\n"
           "LaPicEditor is ideal for users needing\n"
           "advanced control over image editing,\n"
           "particularly in scientific and technical context\n"
            )
            info_label = Label(lap, text=info_text, font=("Arial", 11,"bold"),bg="black",fg="white" ,justify=LEFT).place(x=10, y=60)
            LaPicClose=Button(lap, text="X", width=5, height=1, font=("Arial", 10,"bold"),bg="red",fg="white", command=lap.destroy).place(x=320,y=13)
    button = Button(book,text="Open",width=5,height=1,font=("Arial",10,"bold"),command=LaPicEditor).place(x=230,y=130)
    def Calculator():
            cal=Toplevel(book)
            cal.title("About Calc")
            cal.geometry("390x350+1110+1")
            cal.config(bg="black")
            Calclbl=Label(cal,text="Calc",font=("Arial",20,"bold"),bg="black",fg="white").place(x=110,y=8)
            info_text = (
           "A basic calculator for performing simple\n"
           "arithmetic operations.\n"
           "Designed for quick,everyday calculations\n"
           "without the complexity of advanced functions.\n"
           "It provides the various operations such as\n"
           "addition,subtraction,multiplication,\n"
           "division,modulus division and conjugate\n"
           "for complex numbers.\n"
           "Ideal for users who need a straightforward\n"
           "tool for numbers crunching."
            )
            info_label = Label(cal, text=info_text, font=("Arial", 11,"bold"),bg="black",fg="white", justify=LEFT).place(x=10, y=60)
            CalcClose=Button(cal, text="X", width=5, height=1, font=("Arial", 10,"bold"),bg="red",fg="white",command=cal.destroy).place(x=320,y=13)          
    button = Button(book,text="Open",width=5,height=1,font=("Arial",10,"bold"),command=Calculator).place(x=230,y=190)
    def TimeDate():
            td=Toplevel(book)
            td.title("About Clock")
            td.geometry("390x350+1110+1")
            td.config(bg="black")
            Clocklbl=Label(td,text="Clock",font=("Arial",20,"bold"),bg="black",fg="white").place(x=110,y=2)
            info_text = (
           "A multifunctional tools that provides both\n"
           "date and time functionalities.\n"
           "Useful for keeping track of deadlines and\n"
           "maintaining productivity during tasks.\n"
           "Clean,intuitive clock utility built directly\n"
           "into the LaPY environment."
            )
            info_label = Label(td, text=info_text, font=("Arial", 11,"bold"),bg="black",fg="white", justify=LEFT).place(x=10, y=60)
            TdClose=Button(td, text="X", width=5, height=1, font=("Arial", 10,"bold"),bg="red",fg="white",command=td.destroy).place(x=320,y=13)     
    button = Button(book,text="Open",width=5,height=1,font=("Arial",10,"bold"),command=TimeDate).place(x=230,y=250)
    def Reference():
            rf=Toplevel(book)
            rf.title("About Clock")
            rf.geometry("390x350+1110+1")
            rf.config(bg="black")
            Reflbl=Label(rf,text="Reference",font=("Arial",20,"bold"),bg="black",fg="white").place(x=85,y=8)
            info_text = (
           "Youtube.\n"
           "TechNEO - Advanced Python Programming.\n"
           "by Kapadi Mohammad Saif "
            )
            info_label = Label(rf, text=info_text, font=("Arial", 11,"bold"),bg="black",fg="white", justify=LEFT).place(x=10, y=60)
            RfClose=Button(rf, text="X", width=5, height=1, font=("Arial", 10,"bold"),bg="red",fg="white",command=rf.destroy).place(x=320,y=13)
    button = Button(book,text="Open",width=5,height=1,font=("Arial",10,"bold"),command=Reference).place(x=230,y=310)        
def start():
        start=Toplevel(Lapy)
        start.title("start")
        start.geometry("300x400")
image1=Image.open(r'C:\Users\Saeem\Downloads\lapic.jpg')
resize1=image1.resize((60,60))
bgimg1=ImageTk.PhotoImage(resize1)
LapyLabel=Label(Lapy,text="LaPicEditor",font=("Arial",10)).place(x=12,y=80)
Lapybutton = Button(Lapy, text="LaPicEditor",image=bgimg1, width=50, height=50, font=("Arial", 7), command=PE).place(x=20, y=20)
image2=Image.open(r'C:\Users\Saeem\Downloads\calc.jpg')
resize2=image2.resize((60,60))
bgimg2=ImageTk.PhotoImage(resize2)
CalcLabel=Label(Lapy,text="Calculator",font=("Arial",10)).place(x=106,y=80)
Calcbutton =  Button(Lapy,text="Calc",image=bgimg2,width=50,height=50,font=("Arial",7),command=Calc).place(x=110,y=20)
#image3=Image.open(r'C:\Users\Saeem\OneDrive\Desktop\datetime.jpg')
#resize3=image3.resize((60,60))
#bgimg3=ImageTk.PhotoImage(resize3)
#ClockLabel=Label(Lapy,text="Clock",font=("Arial",10)).place(x=209,y=80)
#ClockButton = Button(Lapy,text="Clock",image=bgimg3,width=50,height=50,font=("Arial",7),command=Clock).place(x=200,y=20)
image4=Image.open(r'C:\Users\Saeem\Downloads\book.jpg')
resize4=image4.resize((60,60))
bgimg4=ImageTk.PhotoImage(resize4)
BookLabel=Label(Lapy,text="Book",font=("Arial",10)).place(x=30,y=180)
BookButton = Button(Lapy,text="Book",image=bgimg4,width=50,height=50,font=("Arial",7),command=Book).place(x=20,y=120)
image5=Image.open(r'D:\Saif.Python\python\Images\filem.jpg')
resize5=image5.resize((60,60))
bgimg5=ImageTk.PhotoImage(resize5)
FileManager=Button(Lapy,text="File Manager",image=bgimg5,width=50,height=50,font=("Arial",70),command=FM).place(x=106,y=120)
image6=Image.open(r'D:\Saif.Python\python\Images\store.jpg')
resize6=image6.resize((60,60))
bgimg6=ImageTk.PhotoImage(resize6)
LaStore=Button(Lapy,text="Lastore",image=bgimg6,width=50,height=50,font=("Arial",70),command=store).place(x=192,y=120)
OpenBtn=Button(Lapy,text="start",font=("Arial",7),bg="red",fg="white",command=start).place(x=10,y=462)
OffButton=Button(Lapy,text="🔌",font=("Arial",7),bg="blue",fg="white",command=Lapy.destroy).place(x=50,y=462)
Lapy.mainloop()


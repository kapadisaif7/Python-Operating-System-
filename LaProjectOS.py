from tkinter import *
from time import strftime
import datetime as dt
import nu
import matplotlib
from matplotlib import pyplot as plt
from PIL import Image, ImageTk
from tkinter import filedialog

# Create the main window
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
    # Create the secondary window for the image editor
    pe = Toplevel(Lapy)  # Use Toplevel to create a child window
    pe.title("LaPicEditor")
    pe.geometry("550x500+970+1")  # Make the window larger to fit the image
    pe.configure(bg="grey")
 
            img_label.place(x=100, y=100)
            
            global img0
            img0 = img
            i1 = np.array(img0)
            result_label.config(text=f"Coordinates of img 1\n{i1[::1]}")
    
    def clear_image():  # Function to clear the image and reset the label
        global img_label
        if img_label:
            img_label.destroy()  # Remove the image label from the window
            img_label = None  # Reset img_label to None
            result_label.config(text="")  # Clear the coordinates text as well
    global img_label1,img_label2
    img_label1=None
    img_label2=None
    def open_file():  # Function for performing image addition, subtraction, and multiplication
        file_path1 = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg")])
        file_path2 = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg")])
    
        if file_path1 and file_path2:  # If both files are selected
           img1 = Image.open(file_path1)
           img2 = Image.open(file_path2)
        
           img1.thumbnail((150, 150))  # Resize both images to fit within the window
           img2.thumbnail((150, 150))
        
           photo1 = ImageTk.PhotoImage(img1)
           photo2 = ImageTk.PhotoImage(img2)
        
           global img_label1, img_label2  # Add global references for both image labels
           if img_label1:
               img_label1.destroy()  # Clear the existing image label if present
           if img_label2:
               img_label2.destroy()
        
           img_label1 = Label(pe, image=photo1)
           img_label2 = Label(pe, image=photo2)
        
           img_label1.image = photo1  # Keep a reference to avoid garbage collection
           img_label2.image = photo2
        
           img_label1.place(x=40, y=100)
           img_label2.place(x=250, y=100)
           global img_path1,img_path2
           img_path1=file_path1
           img_path2=file_path2
    def clear_images():  # Function to clear both images
      global img_label1, img_label2
      if img_label1:
          img_label1.destroy()  # Remove img_label1 from the window
          img_label1 = None
      if img_label2:
          img_label2.destroy()  # Remove img_label2 from the window
          img_label2 = None
    def addimg():
            img11=cv2.imread(img_path1)
            img12=cv2.imread(img_path2)
            height,width,color_scale=img11.shape
            dim=(width,height)
            img12=cv2.resize(img12,dim,interpolation=cv2.INTER_AREA)
            result_label.config(text=f"Original dimension img1:{img11.shape}")
            result_label.config(text=f"Original dimension img2:{img12.shape}")
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
            result_label.config(text=f"Original dimension img1:{img21.shape}")
            result_label.config(text=f"Original dimension img2:{img22.shape}")
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
            result_label.config(text=f"Original dimension img1:{img31.shape}")
            result_label.config(text=f"Original dimension img2:{img32.shape}")
            mul_img=cv2.multiply(img31,img32)
            titles=[ 'image1','image2','multiplied image']
            images=[img31,img32,mul_img]
            for i in range(3):
                   plt.subplot(1,3,i+1),plt.imshow(images[i])
                   plt.title(titles[i])
                   plt.xticks([]),plt.yticks([])
            plt.show()     
    # Button to open the file dialog
    frame2=Frame(pe,width=150,height=1000,bg="yellow").place(x=450,y=0)
    button=Button(pe,text="Upload",height=2,width=10,font=("Arial",8),command=openfile).place(x=465,y=60)
    clear_button = Button(pe, text="Clear Image",height=2,width=10,font=("Arial",8), command=clear_image).place(x=465, y=120)
    button1= Button(pe, text="Get Img", height=2, width=10, font=("Arial", 8), command=open_file).place(x=465, y=200)
    button2=Button(pe,text="Add",height=2,width=10,font=("Arial",8),command=addimg).place(x=465,y=250)
    button3=Button(pges",height=2,width=10,font=("Arial",8), command=clear_images).place(x=465,y=410)
    LapicClose=Button(pe,text="X",height=2,width=8,font=("Arial",8,"bold"),bg="red",fg="white",command=pe.destroy).place(x=465,y=10)
def Calc():
    ce = Toplevel(Lapy)
    ce.title("Calc")
    ce.geometry("400x400+1000+1")
    ce.configure(bg="grey")
    frame3=Frame(ce,width=250,height=325,bg="lightgrey").place(x=75,y=30)
    # Labels and Entry widgets for user input
    num1_entry = Entry(ce,width=35)
    num1_entry.place(x=90, y=40)
    num2_entry = Entry(ce,width=35)
    num2_entry.place(x=90, y=70)

    result_label = Label(ce,width=26, text="", font=("Arial", 10))
    result_label.place(x=90, y=103)

    def add():
        num1_str = num1_entry.get()  # Get input as a string
        num2_str = num2_entry.get()

        # Try to convert input to either int, float, or complex
        try:
            if 'j' in num1_str or 'j' in num2_str:  # Complex number
                num1 = complex(num1_str)
                num2 = complex(num2_str)
            else:  # Normal integer or float
                num1 = float(num1_str) if '.' in num1_str else int(num1_str)
                num2 = float(num2_str) if '.' in num2_str else int(num2_str) 
            # Perform the calculations
            results = (f"{num1 + num2}")
            result_label.config(text=results)  # Update label text with the results
        except ValueError:
            result_label.config(text="Invalid input! ")
    def sub():
       num1_str = num1_entry.get()
       num2_str = num2_entry.get()
       try:
        if 'j' in num1_str or 'j' in num2_str:  # Handle complex numbers
            num1 = complex(num1_str)
            num2 = complex(num2_str)
        else:  # Handle real numbers (float or int)
            num1 = float(num1_str) if '.' in num1_str else int(num1_str)
            num2 = float(num2_str) if '.' in num2_str else int(num2_str)

        # Perform subtraction
        results = f"{num1 - num2}"
        result_label.config(text=results)

       except ValueError:
        result_label.config(text="Invalid Input!")
    def mul():
       num1_str = num1_entry.get()
       num2_str = num2_entry.get()
       try:
        if 'j' in num1_str or 'j' in num2_str:  # Handle complex numbers
            num1 = complex(num1_str)
            num2 = complex(num2_str)
        else:  # Handle real numbers (float or int)
            num1 = float(num1_str) if '.' in num1_str else int(num1_str)
            num2 = float(num2_str) if '.' in num2_str else int(num2_str)

        # Perform subtraction
        results = f"{num1 * num2}"
        result_label.config(text=results)

       except ValueError:
        result_label.config(text="Invalid Input!")
    def div():
       num1_str = num1_entry.get()
       num2_str = num2_entry.get()
       try:
        if 'j' in num1_str or 'j' in num2_str:  # Handle complex numbers
            num1 = complex(num1_str)
            num2 = complex(num2_str)
        else:  # Handle real numbers (float or int)
            num1 = float(num1_str) if '.' in num1_str else int(num1_str)
            num2 = float(num2_str) if '.' in num2_str else int(num2_str)

        # Perform subtraction
        results = f"{num1 / num2}"
        result_label.config(text=results)

       except ValueError:
        result_label.config(text="Invalid Input!")
    def mod():####
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
        try:
          if 'j' in num1_str and not 'j' in num2_str:
              num1 = complex(num1_str)
              results = f"Co2_str:
              result_label.config(text="Enter only one complex number.")
              return
          else:
              result_label.config(text="Only applicable for complex numbers.")
          result_label.config(text=results)

        except ValueError:
            result_label.config(text="Invalid Input!")
    #Buttons to tigger calculations
    button23 = Button(ce, text="+", width=5, height=5, font=("Arial", 10), command=add).place(x=265,y=150)
    button24= Button(ce,text="-",width=5,height=2,font=("Arial",10),command=sub).place(x=145,y=150)
    button25= Button(ce,text="*",width=5,height=2,font=("Arial",10),command=mul).place(x=205,y=150)
    button26= Button(ce,ted"),bg="red",fg="white",command=ce.destroy).place(x=205,y=200)
def Clock():
    clock=Toplevel(Lapy)
    clock.title("Clock")
    clock.geometry("500x500")
    clock.state('zoomed')
    def time():
        string=strftime('%H:%M:%S %p')
        lbl.config(text=string)
        lbl.after(1000,ti
    time()
    def date():
        date=dt.datetime.now()
        lbl=Label(clock,text=f"{date:%A,%B,%d,%Y}",font=("Arial",20))
        lbl.place(x=100,y=400)
    date()
    Clockclose=Button(clock,text="X",width=5,height=2,font=("Arial",10,"bold"),bg="red",fg="white",command=clock.destroy).place(x=205,y=200)
def Book():
    book= Toplevel(Lapy)
    book.title("Book")
    book.geometry("300x350+805+1")
    bgimg=Image.open(r'C:\Users\Saeem\Downloads\library.jpg')
    photo6=ImageTk.PhotoImage(bgimg)
    photo6_label=Label(book, image=photo6).place(x=0,y=0)
    book.photo6=photo6
    booklbl=Label(book,text="Contents",font=("Arial",20)).place(x=2,y=2)
    frame4=Frame(book,width=500,height=55,bg="lightblue").place(x=0,y=55)
    lbl1=Label(book,text="1 .  LaPY",bg="lightblue",font=("Arial",20,"bold")).place(x=5,y=65)
    frame5=Frame(book,width=500,height=55,bg="yellow").place(x=0,y=115)
    lbl2=Label(book,text="2 .  LaPicEditor",bg="yellow",font=("Arial",20,"bold")).place(x=5,y=125)
    frame6=Frame(book,width=500,height=55,bg="lightblue").place(x=0,y=175)
    lbl3=Label(book,text="3 .  Calc",bg="lightblue",font=("Arial",20,"bold")).place(x=5,y=185)
    frame7=Frame(book,,bg="lightblue").place(x=0,y=295)
    lbl6=Label(book,text="5 . Reference",bg="lightblue",font=("Arial",20,"bold")).place(x=5,y=305)
    bookClose=Button(book,text="X",width=5,height=1,font=("Arial",10,"bold"),bg="red",fg="white",command=book.destroy).place(x=230,y=10)
    def LaPY():
        la = Toplevel(book)
        la.title("About LaPY")
        la.geometry("350x350+1110+1")

    # Header Label
        LaPYlbl = Label(la, text="LaPY", font=("Arial", 20, "bold")).place(x=140, y=10)

    # Combined Text Label for a, b, c, and d
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
    # Unified label with all the text
        info_label = Label(la, te##xt=info_text, font=("Arial", 11), justify=LEFT).place(x=10, y=60)
        LaPYClose=Button(la,text="X",width=5,height=1,font=("Arial",10,"bold"),bg="red",fg="white",command=la.destroy).place(x=230,y=10)
    button = Button(book, text="Open", width=5, height=1, font=("Arial", 10), command=LaPY).place(x=230, y=70)
    def LaPicEditor():
            lap=Toplevel(book)
            lap.title("About LaPicEditor")
            lap.geometry("350x350+1110+1")
            LaPiclbl=Label(lap,text="LaPicEditor",font=("Arial",20,"bold")).place(x=110,y=2)
            info_text = (
           "A dynamic image editor enhanced with linear\n"
           "algebra capabalities.\n"
           "Facilitates advanced pixel-level image\n"
           "manipulations using mathematical operations.\n\n"
           "It offers the following functionalities:\n"
           "1. get(): Retrive speci$$WW"fic image data for detailed\n"
           "analysing or editing.\n"
           "2. add(): Adds one image layer over another.\n"
           "3. mul(): Multiplication of two images for\n"
           "pixel-level transformations and effects.\n"
           "4. sub(): Subtraction of one image layer with other.\n"
           "LaPicEditor is ideal for users needing\n"
           "advanced control over image editing,\n"
           "particularly in scientific and technical context\n"
            )
    # Unified label with all the text
            info_label = Label(lap, text=info_text, font=("Arial", 11), justify=LEFT).place(x=10, y=60)
            LaPicClose=Button(lap, text="X", width=5, height=1, font=("Arial", 10,"bold"),bg="red",fg="white", command=lap.destroy).place(x=150, y=310)
    button = Button(book,text="Open",width=5,height=1,font=("Arial",10),command=LaPicEditor).place(x=230,y=130)
    def Calculator():
            cal=Toplevel(book)
            cal.title("About Calc")
            cal.geometry("350x350+1110+1")
            Calclbl=Label(cal,text="Calc",font=("Arial",20,"bold")).place(x=110,y=2)
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
    # Unified label with all the text
            info_label = Label(cal, text=info_text, font=("Arial", 11), justify=LEFT).place(x=10, y=60)
            CalcClose=Button(cal, text="X", width=5, height=1, font=("Arial", 10,"bold"),bg="red",fg="white",command=cal.destroy).place(x=150, y=310)          
    button = Button(book,text="Open",width=5,height=1,font=("Arial",10),command=Calculator).place(x=230,y=190)
    def Tock",font=("Arial",20,"bold")).place(x=110,y=2)
            info_text = (
           "A multifunctional tools that provides both\n"
           "date and time functionalities.\n"
           "Useful for keeping track of deadlines and\n"
           "maintaining productivity during tasks.\n"
           "Clean,intuitive clock utility built directly\n"
           "into the LaPY environment."
            )
    # Unified label with all the text
            info_label = Label(td, text=info_text, font=("Arial", 11), justify=LEFT).place(x=10, y=60)
            LaPYClose=Button(td, text="Close", width=5, height=1, font=("Arial", 10), command=td.destroy).place(x=150, y=310)
            
    button = Button(book,text="Open",width=5,height=1,font=("Arial",10),command=TimeDate).place(x=230,y=250)
    def Reference():
            rf=Toplevel(book)
            rf.title("About Clock")
            rf.geometry("350x350+1110+1")
            Reflbl=Label(rf,text="Reference",font=("Arial",20,"bold")).place(x=110,y=2
            )
    # Unified label with all the text
            info_label = Label(rf, text=info_text, font=("Arial", 11), justify=LEFT).place(x=10, y=60)            
    button = Button(book,text="Open",width=5,height=1,font=("Arial",10),command=Reference).place(x=230,y=310)        
# Button on the main window to open the secondary window
image1=Image.open(r'C:\Users\Sownloads\lapic.jpg')
resize1=image1.resize((60,60))
bgimg1=ImageTk.PhotoImage(resize1)
Lapybutton = Button(Lapy, text="LaPicEditor",image=bgimg1, width=50, height=50, font=("Arial", 7), command=PE).place(x=20, y=20)
image2=Image.open(r'C:\UsersDownloads\calc.jpg')
resize2=image2.resize((60,60))
bgimg2=ImageTk.PhotoImage(resize2)
Calcbutton =  Button(Lapy,text="Calc",image=bgimg2,width=50,height=50,font=("Arial",7),command=Calc).place(x=150,y=20)
image3=Image.open(r'C:\Users\OneDrive\Desktop\datetime.jpg')
resize3=image3.resize((60,60))
bgimg3=ImageTk.PhotoImage(resize3)
ClockButton = Button(Lapy,text="Clock",image=bgimg3,width=50,height=50,font=("Arial",7),command=Clock).place(x=280,y=20)
image4=I=10,height=1,font=("Arial",7),command=Lapy.destroy).place(x=20,y=462)
# Start the Tkinter main event loop


from pyexpat import model
from tkinter import *
from datetime import date
from tkinter.ttk import Combobox
import datetime
import tkinter as tk
from tkinter import ttk
import os
from tkinter import messagebox

import matplotlib
from sklearn import model_selection

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from matplotlib.figure import Figure
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.model_selection import *


from backend import *

from SaveSql import *

from  register import *

from Login import *


background="#f0ddd5"
framebg="#62a7ff"
framefg="#fefbfb" 

root=Tk()
root.title("Heart Attack Prediction System")
#root.geometry("1200x600")
root.geometry("1300x670+30+40")
root.resizable(True,True)
root.config(bg=background)


#########  Analysis <<<<<<<<<<<<<<<<<<<<
def analysis():
    global prediction

    name= Name.get()
    D1= Date.get()
    today = datetime.date.today()
    A = today.year-DOB.get()

    try:
        B=selection()
    except:
        messagebox.showerror("Missing","Please select gender!!")
        return
    
    try:
        F=selection2()
    except:
        messagebox.showerror("Missing","Please select fbs!!")
        return
    
    try:
        I=selection3()
    except:
        messagebox.showerror("Missing","Please select exang!!")
        return
    
    try:
        C=int(selection4())
    except:
        messagebox.showerror("Missing","Please select cp!!")
        return
    
    try:
        G=int(restecg_combobox.get())
    except:
        messagebox.showerror("Missing","Please select restecg!!")
        return
    
    try:
        K=int(selection5())
    except:
        messagebox.showerror("Missing","Please select slope!!")
        return
    
    try:
        L=int(ca_combobox.get())
    except:
        messagebox.showerror("Missing","Please select ca!!")
        return
    
    try:
        M=int(thal_combobox.get())
    except:
        messagebox.showerror("Missing","Please select thal!!")
        return
    
    try:
        D=int(trestbps.get())
        E=int(chol.get())
        H=int(thalach.get())
        J=int(oldpeak.get())
    except:
        messagebox.showerror("Missing data","Few missing data entry!!")
        return

## checking for work 
    
    print("A is age :", A)
    print("B is gender :", B)
    print("C is cp :", C)
    print("D is trestbps :", D)
    print("E is chol :", E)
    print("F is fbs :", F)
    print("G is restcg :", G)
    print("H is thalach", H)
    print("I is Exang :", I)
    print("J is oldpeak :", J)
    print("K is slop :", K)
    print("L is ca :", L)
    print("M is thal :", M)


    ######   First graph   #######
    f = Figure(figsize=(5,5),dpi=100)
    a = f.add_subplot(111)
    a.plot(["Sex","fbs","exang"],[B,F,I])
    canvas = FigureCanvasTkAgg(f)
    canvas.get_tk_widget().pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)
    canvas._tkcanvas.place(width=200,height=180,x=530,y=230)

    ######   Second Graph  ########
    f2 = Figure(figsize=(5,5),dpi=100)
    a2 = f2.add_subplot(111)
    a2.plot(["age","trestbps","chol","thalach"],[A,D,E,H])
    canvas2 = FigureCanvasTkAgg(f2)
    canvas2.get_tk_widget().pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)
    canvas2._tkcanvas.place(width=200,height=180,x=760,y=230)
    
    ######   third Graph ########
    f3 = Figure(figsize=(5,5),dpi=100)
    a3 = f3.add_subplot(111)
    a3.plot(["oldpeak","resticg","cp"],[J,G,C])
    canvas3 = FigureCanvasTkAgg(f3)
    canvas3.get_tk_widget().pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)
    canvas3._tkcanvas.place(width=200,height=180,x=530,y=440)

    ######   fourth Graph ########
    f4 = Figure(figsize=(5,5),dpi=100)
    a4 = f4.add_subplot(111)
    a4.plot(["slope","ca","thal"],[K,L,M])
    canvas4 = FigureCanvasTkAgg(f4)
    canvas4.get_tk_widget().pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)
    canvas4._tkcanvas.place(width=200,height=180,x=760,y=440)



    #input data
    input_data = (A,B,C,D,E,F,G,H,I,J,K,L,M)

    input_data_as_numpy_array=np.asanyarray(input_data)

    #reshape the numpy array as ew are predicting for only one instance
    
    input_data_reshape = input_data_as_numpy_array.reshape(1,-1)

    prediction = model.predict(input_data_reshape)
    print(prediction)

    if (prediction[0]==0):
        print("The Person does not have a Heart Disease")
        report.config(text=f"Report:{0}",fg="#8dc63f")
        report1.config(text=f"{name} You do not have a heart disease")

    else:
        print("The Person have a Heart Disease")
        report.config(text=f"Report:{1}",fg="#ed1c24")
        report1.config(text=f"{name} You have a heart disease")



##info_window (operated by info button)///////////////////
def Info():
    Icon_window=Toplevel(root)
    Icon_window.title("Info")
    Icon_window.geometry("700x600+100+100")

    #icon_image
    icon_image=PhotoImage(file="Images\info.png")
    Icon_window.iconphoto(False,icon_image)

    #Heading
    Label(Icon_window,text="Information Related to dataset",font="robot 17 bold").pack(padx=20,pady=20)

    #info
    Label(Icon_window,text="age: Age of the individual.",font="arial 11").place(x=20,y=100)
    Label(Icon_window,text="sex: Gender of the individual (1 = male, 0 = female)",font="arial 11").place(x=20,y=130)
    Label(Icon_window,text="cp: Chest pain type (typically classified into categories like 0, 1, 2, 3).",font="arial 11").place(x=20,y=160)
    Label(Icon_window,text="trestbps: Resting blood pressure (in mm Hg).",font="arial 11").place(x=20,y=190)
    Label(Icon_window,text="chol: Serum cholesterol level (in mg/dl).",font="arial 11").place(x=20,y=220)
    Label(Icon_window,text="fbs: Fasting blood sugar > 120 mg/dl (1 = true, 0 = false).",font="arial 11").place(x=20,y=250)
    Label(Icon_window,text="restecg: Resting electrocardiographic results (commonly categorized).",font="arial 11").place(x=20,y=280)
    Label(Icon_window,text="thalach: Maximum heart rate achieved.",font="arial 11").place(x=20,y=310)
    Label(Icon_window,text="exang: Exercise induced angina (1 = yes, 0 = no).",font="arial 11").place(x=20,y=340)
    Label(Icon_window,text="oldpeak: ST depression induced by exercise relative to rest.",font="arial 11").place(x=20,y=370)
    Label(Icon_window,text="slope: The slope of the peak exercise ST segment.",font="arial 11").place(x=20,y=400)
    Label(Icon_window,text="ca: Number of major vessels (0-3) colored by fluoroscopy.",font="arial 11").place(x=20,y=430)
    Label(Icon_window,text="thal: Thalassemia (a blood disorder) type.",font="arial 11").place(x=20,y=460)
    Label(Icon_window,text="target: Presence or absence of heart disease (1 = presence, 0 = absence).",font="arial 11").place(x=20,y=490)



    Icon_window.mainloop()
    
    
###Save Data<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def Save():
    # A2=Registration.get()
    B2=Name.get()
    C2=Date.get()
    D2=DOB.get() 

    today = datetime.date.today()
    E2=today.year-DOB.get()    #age
    
    try:
        F2=selection()
    except:
        messagebox.showerror("Missing Data","Please Select gender!")
        return
     
    try:
        J2=selection2()
    except:
        messagebox.showerror("Missing Data","Please Select fbs!")
        return
    
    try:
        M2=selection3()
    except:
        messagebox.showerror("Missing Data","Please Select Exang!")
        return
    
    try:
        G2=selection4()
    except:
        messagebox.showerror("Missing Data","Please select cp!")
        return
    
    try:
        K2=restecg_combobox.get()
    except:
        messagebox.showerror("Missing Data","Please select restcg!")
        return
    
    try:
        O2=selection5()
    except:
        messagebox.showerror("Missing Data","Please select slope!")
        return
    
    try:
        P2=ca_combobox.get()
    except:
        messagebox.showerror("Missing Data","Please select ca!")
        return
    
    try:
        Q2=thal_combobox.get()
    except:
        messagebox.showerror("Missing Data","Please select thal")
        return

    H2=trestbps.get()
    I2=chol.get()
    L2=thalach.get()
    N2=float(oldpeak.get())
    
    ##calling from savesql
    Save_Data_MySql(B2,C2,int(D2),int(E2),int(F2),int(G2),int(H2),int(I2),int(J2),int(K2),int(L2),int(M2),float(N2),int(O2),int(P2),int(Q2),int(prediction[0]))

    Clear()

    root.destroy()

    os.system("main.py")




#$$$$$$$$$$$$$$$$$$$$$$$$$$$

######### Used for closing window ##########
def logout():
    root.destroy()


######  Clear ( with the help of clear we can clear more entry fields in once)
def Clear():
    Name.get('')
    DOB.get('')
    trestbps.get('')
    chol.get('')
    thalach.get('')
    oldpeak.set('')




#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#icon 1
image_icon=PhotoImage(file="Images/icon.png")
root.iconphoto(False,image_icon)

# header section 
logo=PhotoImage(file="Images/header.png",height=400)
myimage=Label(image=logo,bg=background)
myimage.place(x=0,y=-30)

##frame 3
Heading_entry=Frame(root,width=600,height=150,bg="#df2d4b")
Heading_entry.place(x=600,y=20)

Label(Heading_entry,text="Registration No.",font="arial 13",bg="#df2d4b",fg=framefg).place(x=30,y=0)
Label(Heading_entry,text="Date",font="arial 13",bg="#df2d4b",fg=framefg).place(x=300,y=0)

Label(Heading_entry,text="Patient Name",font="arial 13",bg="#df2d4b",fg=framefg).place(x=30,y=90)
Label(Heading_entry,text="Birth Year",font="arial 13",bg="#df2d4b",fg=framefg).place(x=300,y=90)

#Entry_image=PhotoImage(file="Images/Rounded Rectangle 1.png")
#Entry_image2=PhotoImage(file="Images/Rounded Rectangle 2.png")
Label(Heading_entry,bg="#df2d4b").place(x=20,y=30)
Label(Heading_entry,bg="#df2d4b").place(x=430,y=30)

Label(Heading_entry,bg="#df2d4b").place(x=20,y=90)
Label(Heading_entry,bg="#df2d4b").place(x=430,y=90)

Registration=IntVar()
reg_entry= Entry(Heading_entry,textvariable=Registration,width=15,font="arial 15",bg="#0e5363",fg="white",bd=0)
reg_entry.place(x=30,y=35)

Date = StringVar()
today = date.today()
d1 = today.strftime("%d/%m/%Y")
data_entry= Entry(Heading_entry,textvariable=Date,width=15,font="arial 15",bg="#0e5363",fg="white",bd=0)
data_entry.place(x=300,y=35)
Date.set(d1)

Name= StringVar()
name_entry= Entry(Heading_entry,textvariable=Name,width=11,font="arial 20",bg="#ededed",fg="#222222",bd=0)
name_entry.place(x=30,y=120)

DOB= IntVar()
dob_entry= Entry(Heading_entry,textvariable=DOB,width=11,font="arial 20",bg="#ededed",fg="#222222",bd=0)
dob_entry.place(x=300,y=120)




##########################  Body ##########################
Detail_entry=Frame(root,width=490,height=260,bg="#dbe0e3")
Detail_entry.place(x=30,y=400)


###################### Radio Button ####################
Label(Detail_entry,text="sex:",font="arial 13",bg=framebg,fg=framefg).place(x=10,y=10)
Label(Detail_entry,text="fbs:",font="arial 13",bg=framebg,fg=framefg).place(x=180,y=10)
Label(Detail_entry,text="exang:",font="arial 13",bg=framebg,fg=framefg).place(x=335,y=10)

def selection():
    if gen.get()==1:
        Gender=1
        return(Gender)
        print(Gender)
    elif gen.get()==2:
        Gender=2
        return(Gender)
        print(Gender)
    else:
        print(Gender)


def selection2():
    if fbs.get()==1:
        Fbs=1
        return(Fbs)
        print(Fbs)
    elif fbs.get()==2:
        Fbs=2
        return(Fbs)
        print(Fbs)
    else:
        print(Fbs)


def selection3():
    if exang.get()==1:
        Exang=1
        return(Exang)
        print(Exang)
    elif exang.get()==2:
        Gender=2
        return(Exang)
        print(Exang)
    else:
        print(Exang)

gen = IntVar()
R1 = Radiobutton(Detail_entry,text='Male',variable=gen,value=1,command=selection)
R2 = Radiobutton(Detail_entry,text='Female',variable=gen,value=2,command=selection)
R1.place(x=43,y=10)
R2.place(x=93,y=10)

fbs = IntVar()
R3 = Radiobutton(Detail_entry,text='True',variable=fbs,value=1,command=selection2)
R4 = Radiobutton(Detail_entry,text='False',variable=fbs,value=2,command=selection2)
R3.place(x=215,y=10)
R4.place(x=265,y=10)

exang = IntVar()
R5 = Radiobutton(Detail_entry,text='Yes',variable=exang,value=1,command=selection3)
R6 = Radiobutton(Detail_entry,text='No',variable=exang,value=2,command=selection3)
R5.place(x=385,y=10)
R6.place(x=430,y=10)

################  Combo Box ############     6

Label(Detail_entry,text="cp",font="arial 13",bg=framebg,fg=framefg).place(x=10,y=50)
Label(Detail_entry,text="restecg",font="arial 13",bg=framebg,fg=framefg).place(x=10,y=90)
Label(Detail_entry,text="slope",font="arial 13",bg=framebg,fg=framefg).place(x=10,y=130)
Label(Detail_entry,text="ca",font="arial 13",bg=framebg,fg=framefg).place(x=10,y=170)
Label(Detail_entry,text="thal",font="arial 13",bg=framebg,fg=framefg).place(x=10,y=210)

def selection4():
    input=cp_combobox.get()
    if input=="0 = typical angina":
        return(0)
    elif input=="1 = atypical angina":
        return(1)
    elif input=="2 = non-anginal pain":
        return(2)
    elif input=="3 = asymptomatic":
        return(3)
    else:
        print(exang)


def selection5():
    input=slope_combobox.get()
    if input=="0 = upsloping":
        return(0)
    elif input=="1 = flat":
        return(1)
    elif input=="2 = downsloping":
        return(2)
    else:
        print(exang)




cp_combobox=Combobox(Detail_entry,values=['0 = typical angina','1 = atypical angina', '2 = non-anginal pain', '3 = asymptomatic'],font="arial 12",state="r",width=11)
restecg_combobox=Combobox(Detail_entry,values=['0','1','2'],font="arial 12",state="r",width=11)
slope_combobox=Combobox(Detail_entry,values=['0 = upsloping','1 = flat', '2 = downsloping'],font="arial 12",state="r",width=11)
ca_combobox=Combobox(Detail_entry,values=['0','1','2','3','4'],font="arial 12",state="r",width=11)
thal_combobox=Combobox(Detail_entry,values=['0','1','2','3',],font="arial 12",state="r",width=11)


cp_combobox.place(x=50,y=50)
restecg_combobox.place(x=80,y=90)
slope_combobox.place(x=70,y=130)
ca_combobox.place(x=50,y=170)
thal_combobox.place(x=50,y=210)



#######################   Data Entry Box ###########################    7

Label(Detail_entry,text="Smoking:",font="arial 13",width=7,bg="#dbe0e3",fg="black").place(x=240,y=50)
Label(Detail_entry,text="trestbps:",font="arial 13",width=7,bg=framebg,fg=framefg).place(x=240,y=90)
Label(Detail_entry,text="chol:",font="arial 13",width=7,bg=framebg,fg=framefg).place(x=240,y=130)
Label(Detail_entry,text="thalach:",font="arial 13",width=7,bg=framebg,fg=framefg).place(x=240,y=170)
Label(Detail_entry,text="oldpeak:",font="arial 13",width=7,bg=framebg,fg=framefg).place(x=240,y=210)

trestbps=StringVar()
chol=StringVar()
thalach=StringVar()
oldpeak=StringVar()

trestbps_entry= Entry(Detail_entry,textvariable=trestbps,width=10,font="arial 15",bg="#ededed",fg="#222222",bd=0)
chol_entry= Entry(Detail_entry,textvariable=chol,width=10,font="arial 15",bg="#ededed",fg="#222222",bd=0)
thalach_entry= Entry(Detail_entry,textvariable=thalach,width=10,font="arial 15",bg="#ededed",fg="#222222",bd=0)
oldpeak_entry= Entry(Detail_entry,textvariable=oldpeak,width=10,font="arial 15",bg="#ededed",fg="#222222",bd=0)

trestbps_entry.place(x=320,y=90)
chol_entry.place(x=320,y=130)
thalach_entry.place(x=320,y=170)
oldpeak_entry.place(x=320,y=210)



########################   Report #########################    8
square_report_image=PhotoImage(file="Images\Report.png")
report_background=Label(image=square_report_image,bg=background)
report_background.place(x=1030,y=265)

report=Label(root,font="arial 25 bold", bg="white",fg="#8dc63f")
report.place(x=1070,y=480)

report1=Label(root,font="arial 10 bold",bg="white")
report1.place(x=1038,y=550)



############################## Graph ###########################   9
graph_image=PhotoImage(file="Images\graph.png")
Label(image=graph_image,height=180,width=200).place(x=530,y=230)
Label(image=graph_image,height=180,width=200).place(x=760,y=230)
Label(image=graph_image,height=180,width=200).place(x=530,y=440)
Label(image=graph_image,height=180,width=200).place(x=760,y=440)

####################  Analysis Button ###########################   10
analysis_button=PhotoImage(file="Images\Analysis.png")
Button(root,image=analysis_button,bd=0,bg=background,cursor='hand2',command=analysis).place(x=990,y=197)

#### info button ######

info_button=PhotoImage(file="Images\info.png")
Button(root,image=info_button,bd=0,bg=background,cursor='hand2',command=Info).place(x=10,y=240)


#### save button ######

save_button=PhotoImage(file="Images\save.png")
Button(root,image=save_button,bd=0,bg=background,cursor='hand2',command=Save).place(x=1200,y=210)

#############  Smoking and Non Smoking Button ############   11
button_mode= True
choice="smoking"
def changemode():
    global button_mode
    global choice

    if button_mode:
        choice="non_smoking"
        mode.config(image=non_smoking_icon,activebackground="white")
        button_mode=False
    else:
        choice="smoking"
        mode.config(image=smoking_icon,activebackground="white")
        button_mode=True

    print(choice)

smoking_icon=PhotoImage(file="Images/smoker.png")
non_smoking_icon=PhotoImage(file="Images/nonsmoker.png")
mode=Button(root,image=smoking_icon,bg="#dbe0e3",bd=0,cursor="hand2",command=changemode)
mode.place(x=350,y=446)


#################################################################################

############################### LogOut Button ############ 12

logout_icon=PhotoImage(file="Images/logout.png")
logout_button=Button(root,image=logout_icon,bg="#df2d4b",cursor="hand2",bd=0,command=logout)
logout_button.place(x=1140,y=60)

##############################################################
















root.mainloop()
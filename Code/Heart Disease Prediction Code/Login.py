from tkinter import *
from tkinter import messagebox
import mysql.connector
import os 



root=Tk()
root.title("Login Page")
root.geometry("1450x730+60+80")
root.resizable(False,False)
# root.configure(bg="#111315")


#color
bc="#111119"
framebg="#EDEDED" #283055
framefg="#06283D"




###Trial ##########
global trial_no
trial_no=0

def trial():
    global trial_no

    trial_no +=1
    print("Trial no is ",trial_no)
    if trial_no==3:
        messagebox.showwarning("Warning","You have tried more then limit!!")
        root.destroy()  #program close

######################################################3


def signin():
    username=user.get()
    password=code.get()

    if (username=="" or username=="Username") or (password=="" or password=="Password"):
        messagebox.showerror("Entry error","Type username or password!!")

    else:
        try:
            mydb=mysql.connector.connect(host='localhost',user='root',password='Kishore@12345678',database="heart_data")
            mycursor=mydb.cursor()
            print("Connected to Database!!")
            


        except:
            messagebox.showerror("Connection","Database connection not establish!!")
            return

        command="use heart_data"
        mycursor.execute(command)

        command="select * from login where Username=%s and Password=%s"
        mycursor.execute(command,(username,password))
        myresult =mycursor.fetchone()
        print(myresult)

        if myresult==None:

            messagebox.showinfo("invalid","Invalid userid and password!!")

            #but user can try many times and crack password, so lets make that user can try only upto 3 times

            trial()

        else:
            messagebox.showinfo("Login","Sucessfully Login!!!")

            root.destroy()

            import main

    

    
def signup_command():
    root.destroy()
    os.system("register.py")
    



#icon
image_icon=PhotoImage(file="Images/icon.png")
root.iconphoto(False,image_icon)

#header
logo=PhotoImage(file="Images/header.png")
myimage=Label(image=logo)
myimage.place(x=0,y=0)




frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=600,y=300)

heading=Label(frame,text='Sign in',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)

#########------------------------------------------------------

def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')

        
user = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

###########-----------------------------------------------------
def on_enter(e):
    code.delete(0, 'end')  

def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Password')



code = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

###############################################################

Button(frame,width=39,pady=7,text='Sign in',bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=204)
label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=75,y=270)

sign_up= Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=signup_command)
sign_up.place(x=215,y=270)



root.mainloop()





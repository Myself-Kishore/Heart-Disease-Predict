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



def signup():
    username=user.get()
    password=code.get()
    confirm_password=confirm_code.get()

    print(username,password,confirm_password)
 

    if (username=="" or username=="UserID") or (password=="" or password=="Password"):
            messagebox.showerror("Entry error!", "Type username or password !!!")
    
    else:
        if password==confirm_password:

            try:
                mydb = mysql.connector.connect(host='localhost',user='root',password='Kishore@12345678')
                mycursor =mydb.cursor()
                print("Connection Established!!")


            except:
                messagebox.showerror("Connection","Database connection not established !")


            try:
                command="create database heart_data"
                mycursor.execute(command)

                command="use heart_data"
                mycursor.execute(command)

                command="create table login (user int auto_increment key not null, Username varchar(50),Password varchar(100))"
                mycursor.execute(command)


            except:
                mycursor.execute("use heart_data")
                mydb= mysql.connector.connect(host='localhost',user='root',password='Kishore@12345678',database="heart_data")
                mycursor =mydb.cursor()

                command="insert into login(Username,Password) values(%s,%s)"

                mycursor.execute(command,(username,password))
                mydb.commit()
                mydb.close()
                messagebox.showinfo("Register","New User added Sucessfully!!!!")
                Signin()
                


        
        else:
            messagebox.showinfo("info!","Both Password are different!!")

        


def Signin():
    root.destroy()
    os.system("Login.py")




#icon
image_icon=PhotoImage(file="Images/icon.png")
root.iconphoto(False,image_icon)

#header
logo=PhotoImage(file="Images/header.png")
myimage=Label(image=logo)
myimage.place(x=0,y=0)




frame=Frame(root,width=350,height=390,bg='#fff')
frame.place(x=600,y=300)


heading=Label(frame,text='Sign up',fg="#57a1f8",bg='white',font=('Microsoft Yahei UI Light',23,'bold'))
heading.place(x=100,y=5)

#####--------------------------------------------------------
def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    if user.get()=='':
        user.insert(0,'Username')

user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
user.place(x=30,y=80)
user.insert(0, 'Username')
user.bind("<FocusIn>",on_enter)
user.bind("<FocusOut>", on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

#####--------------------------------------------------------
def on_enter(e):
    code.delete(0,'end')
def on_leave(e):
    if code.get()=='':
        code.insert(0,'Password')

code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
code.place(x=30,y=150)
code.insert(0, 'Password')
code.bind("<FocusIn>",on_enter)
code.bind("<FocusOut>", on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

#####--------------------------------------------------------
def on_enter(e):
    confirm_code.delete(0,'end')
def on_leave(e):
    if confirm_code.get()=='':
        confirm_code.insert(0,'Confirm Password')

confirm_code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
confirm_code.place(x=30,y=220)
confirm_code.insert(0, 'Confirm Password')
confirm_code.bind("<FocusIn>",on_enter)
confirm_code.bind("<FocusOut>", on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)

#----------------------------

Button(frame,width=39,pady=7,text='Sign up',bg='#57a1f8',fg='white',border=0,command=signup).place(x=35,y=280)
label=Label(frame,text='I have an account',fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=90,y=340)

signin=Button(frame,width=6,text='Sign in',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=Signin)
signin.place(x=200,y=340)






root.mainloop()

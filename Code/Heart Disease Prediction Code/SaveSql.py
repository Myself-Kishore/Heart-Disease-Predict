import mysql.connector
from tkinter import messagebox

###########################Save#####################

def Save_Data_MySql(B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R):

    try:
        mydb = mysql.connector.connect(host='localhost',user='root',password='Kishore@12345678')
        mycursor =mydb.cursor()
        print("Connection Established!!")

        # // type your passworkd here Kishore@12345678
    

    except:
        messagebox.showerror("Connection","Database connection not established !")

    
    try:
        # print(B)
        # print(C)
        # print(D)
        # print(E)
        # print(F)
        # print(G)
        # print(H)
        # print(I)
        # print(J)
        # print(K)
        # print(L)
        # print(M)
        # print(N)
        # print(O)
        # print(P)
        # print(Q)
        # print(R)
        








        # # command="create database Heart_Data"
        # # mycursor.execute(command)

        command="use Heart_Data"
        mycursor.execute(command)

        command="create table data(user int auto_increment key not null, Name varchar(50),Date varchar(100),DOB varchar(100),age varchar(100),sex varchar(100),Cp varchar(100),trestbps varchar(100),chol varchar(100),fbs varchar(100),restecg varchar(100),thalach varchar(100),exang varchar(100),oldpeak varchar(100),slope varchar(100),ca varchar(100),thal varchar(100),result varchar(100))"
        mycursor.execute(command)

        command="insert into data(Name,Date,DOB,age,sex,Cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal,Result) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        mycursor.execute(command,(B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R))
        mydb.commit()
        mydb.close()
        messagebox.showinfo("Register","New User added Sucessfully!!!!")

        

    except:
        mycursor.execute("use Heart_Data")
        mydb= mysql.connector.connect(host='localhost',user='root',password='Kishore@12345678',database="Heart_Data")
        mycursor =mydb.cursor()

        command="insert into data(Name,Date,DOB,age,sex,Cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal,Result) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        mycursor.execute(command,(B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R))
        mydb.commit()
        mydb.close()
        messagebox.showinfo("Register","New User added Sucessfully!!!!")


        

    





####################Registration NO.#######################
#it is created to automatic enter registration no.

# Save_Data_MySql('mr unknown',"08/08/2023","1979","44","1","1","233","233","1","1","233","1","233.0","0","2","1","0")
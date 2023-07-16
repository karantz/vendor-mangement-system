from tkinter import *
from  tkinter import  ttk
import  mysql.connector as m
import time
import random
import user_inventory as use
t=time.asctime(time.localtime(time.time()))
db=m.connect(host="localhost",user="root",passwd="12345")
c=db.cursor()
c.execute("create database if not existS pythondata")
c.execute("Use pythondata")
c.execute("CREATE table if not existS user_au(NAME VARCHAR(30),CONTACT VARCHAR(30),EMAIL VARCHAR(30),PASSWORD VARCHAR(30),GENDER VARCHAR(30),CITY VARCHAR(30),STATE VARCHAR(30))")
def reg():
    def record():
        name1=name.get()
        con1=contact.get()
        email1=email.get()
        gen1=gender.get()
        city1=city.get()
        state1=state.get()
        pass1=password.get()
        if name1=='' or con1==''or email1=='' or gen1==''or city1==''or state1==''or pass1=='':
            message.set("fill the empty field!!!")
        else:
           insert_stmt = (
               "INSERT INTO user_au(NAME, CONTACT, EMAIL, PASSWORD, GENDER, CITY, STATE)"
               "VALUES (%s, %s, %s, %s, %s, %s, %s)"
           )
           if gen1==1:
            data = (name1, con1,email1,pass1,"Male",city1,state1)
           else:
            data = (name1, con1, email1,pass1, "Female", city1, state1)
           try:
               c.execute(insert_stmt,data)
               db.commit()
           except:
               db.rollback()
           message.set("Stored successfully")
    def log():
        registration.destroy()
        login()
    registration=Tk()
    registration.title("Registration Form")
    registration.geometry("350x400")
    name = StringVar()
    contact = StringVar()
    email=StringVar()
    gender=IntVar()
    city=StringVar()
    state=StringVar()
    message=StringVar()
    password=StringVar()
    Label(registration,width="300", text="Please enter details below", bg="orange",fg="white").pack()
    Label(registration, text="Name * ").place(x=20,y=40)
    Entry(registration, textvariable=name).place(x=90,y=42)
    Label(registration, text="Contact * ").place(x=20,y=80)                         
    Entry(registration, textvariable=contact).place(x=90,y=82)
    Label(registration, text="Email * ").place(x=20, y=120)
    Entry(registration, textvariable=email).place(x=90, y=122)
    Label(registration, text="Password * ").place(x=20, y=160)
    Entry(registration, textvariable=password,show='*').place(x=90, y=162)
    Label(registration, text="Gender * ").place(x=20, y=200)
    Radiobutton(registration,text="Male",variable=gender,value=1).place(x=90,y=200)
    Radiobutton(registration, text="Female", variable=gender, value=2).place(x=150, y=200)
    Label(registration, text="City * ").place(x=20, y=240)
    monthchoosen = ttk.Combobox(registration, width=27, textvariable=city)
    monthchoosen['values'] = (' Mumbai',
                              ' Bhopal',
                              ' Patna',
                              ' Indore',
                              ' Nagpur',
                              ' Pune',
                              ' Gwalior',
                              ' Jabalpur',)
    monthchoosen.current()
    monthchoosen.place(x=90,y=242)
    Label(registration, text="State * ").place(x=20, y=280)
    monthchoosen = ttk.Combobox(registration, width=27, textvariable=state)
    monthchoosen['values'] = (' Madhya Pradesh',
                              ' Maharashtra',
                              ' Bihar',
                              ' Punjab',
                              ' Gujrat',
                              ' Rajsthan',)
    monthchoosen.current()
    monthchoosen.place(x=90, y=282)
    Label(registration, text="",textvariable=message).place(x=95,y=310)
    Button(registration, text="Register", width=10, height=1, bg="orange",command=record).place(x=95,y=340)
    Button(registration, text="Login", width=10, height=1, bg="orange",command=log).place(x=195,y=340)
    
    registration.mainloop()

def login():
    def verify():
        email1=ema.get()
        password1=pas.get()
        
        if email1=='' or password1=='':
            mess.set('EMAIL or PASSWORD EMPTY!!!')
        else:
            q="select password from user_au where email='"+email1+"'"
            c.execute(q)
            p=('',)
            for i in c:
                p=i
            pword=p[0]
            if pword==password1:
                logs.destroy()
                use.user_i()
            else:
                mess.set('WRONG PASSWORD')
                res()
    def res():
        ema.set('')
        pas.set('')
    def back():
        logs.destroy()
        reg()
    logs=Tk()
    logs.title("Login Page")
    logs.geometry("350x400")
    mess=StringVar()
    ema=StringVar()
    pas=StringVar()
    Label(logs,width="300",text="Login Page",bg="orange",fg="white").pack()
    Label(logs,text=t,bg="orange",fg="white").place(x=110,y=40)
    Label(logs,text="Email * ",bg="orange",fg="white",font=("arial",10,"bold")).place(x=30,y=80)
    Entry(logs,bg="white",justify="center",textvariable=ema).place(x=150,y=80)
    Label(logs,bg="orange",fg="white",text="Password *",font=("arial",10,"bold")).place(x=30,y=110)
    Entry(logs,bg="white",justify="center",textvariable=pas,show='*').place(x=150,y=110)
    Button(logs,text="<- back  ",width=5,bg="orange",command=back).place(x=10,y=30)
    Label(logs, text="",textvariable=mess).place(x=90,y=190)
    Button(logs,text="Login",width=10,bg="orange",command=verify).place(x=120,y=150)
    logs.mainloop()

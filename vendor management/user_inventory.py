from tkinter import *
from  tkinter import  ttk
import  mysql.connector as m
import time
import random
from tkinter import messagebox
t=time.asctime(time.localtime(time.time()))
db=m.connect(host="localhost",user="root",passwd="12345")
c=db.cursor()
c.execute("create database if not existS pythondata")
c.execute("Use pythondata")
c.execute("CREATE table if not existS user_au(NAME VARCHAR(30),CONTACT VARCHAR(30),EMAIL VARCHAR(30),PASSWORD VARCHAR(30),GENDER VARCHAR(30),CITY VARCHAR(30),STATE VARCHAR(30))")
c.execute("CREATE table if not existS user_orders(cust_id varchar(10),product_name varchar(30),price varchar(5))")
c.execute("create table if not exists products(product_name varchar(30),price varchar(5))")
c.execute("CREATE table if not existS bill(cust_id varchar(10),total varchar(5))")
r=random.randrange(11111,99999)
        
def user_i():
    def pla():
        order.destroy()
        placed()
    def out():
        messagebox.showinfo('Log out','Logged Out')
        order.destroy()
    def sho():
        order.destroy()
        show()
    order=Tk()
    order.title("Customer Order")
    order.geometry("200x200")
    Label(order,width="200", text="ORDER", bg="orange",fg="white").pack()
    Label(order,width="200", text=t, bg="orange",fg="white").pack()
    Label(order,text='Cust_id :', bg="orange",fg="white").place(x=75,y=60)
    Label(order,text=r, bg="orange",fg="white").place(x=120,y=60)
    Button(order, text="Place Order", width=10, height=1, bg="orange",command=pla).place(x=75,y=90)
    Button(order, text="Show Order", width=10, height=1, bg="orange",command=sho).place(x=75,y=120)
    Button(order, text="Log out", width=10, height=1, bg="orange",command=out).place(x=75,y=150)
    order.mainloop()

def placed():
    def ba():
        place.destroy()
        user_i()
    def od():
        def bi():
            Label(place,text='TOTAL',fg='black').place(x=155,y=m+30)
            Label(place,text=total,fg='black').place(x=255,y=m+30)
            qs="Insert into bill values('"+str(r)+"','"+str(total)+"')"
            c.execute(qs)
            db.commit()
        od=ordes.get()
        q="select price from products where product_name='"+od+"'"
        c.execute(q)
        pr=('',)
        for j in c:
            pr=j
        pri=pr[0]
        qr="insert into user_orders values('"+str(r)+"','"+str(od)+"','"+str(pri)+"')"
        c.execute(qr)
        db.commit()
        Label(place,text='Item Name',bg='orange',fg='white').place(x=155,y=180)
        Label(place,text='Price',bg='orange',fg='white').place(x=255,y=180)
        qrys="select * from user_orders where cust_id='"+str(r)+"'"
        a=-1
        b=0
        m=240
        c.execute(qrys)
        for k in c:
            Label(place,text=k[a+2],fg='black').place(x=155,y=m)
            Label(place,text=k[b+2],fg='black').place(x=255,y=m)
            m=m+30
        qy="select price from user_orders where cust_id='"+str(r)+"'"
        c.execute(qy)
        d=-1
        l=('',)
        
        total=0
        for l in c:
            total=int(l[d+1])+total
        Button(place, text="Bill", width=10, height=1, bg="orange",command=bi).place(x=250,y=150)
        
    place=Tk()
    total=0
    place.title("STOCK")
    place.geometry('1500x1500')
    ordes=StringVar()
    
    Label(place,width="1500",text="MENU",bg='orange',fg='white').pack()
    Label(place,width="1500",text=t,bg='orange',fg='white').pack()
    Label(place,text='Item Name',bg='orange',fg='white').place(x=900,y=80)
    Label(place,text='Price',bg='orange',fg='white').place(x=1200,y=80)
    Entry(place,textvariable=ordes,bg="white",justify="center").place(x=155,y=120)
    Button(place, text="Add", width=10, height=1, bg="orange",command=od).place(x=130,y=150)
   
    qry="select * from products"
    m=120
    a=-2
    b=-1
    c.execute(qry)
    for i in c:
        Label(place,text=i[a+2],fg='black').place(x=900,y=m)
        Label(place,text=i[b+2],fg='black').place(x=1200,y=m)
        m=m+30
    Button(place,text='<-- BACK',width=8,bg='orange',command=ba).place(x=10,y=50)
    place.mainloop()
    
def show():
    def uses():
        show.destroy()
        user_i()
    def os():
        odid=ids.get()
        Label(show,text='Item Name',bg='orange',fg='white').place(x=155,y=160)
        q="select product_name from user_orders where cust_id='"+str(odid)+"'"
        c.execute(q)
        b=-1
        m=190
        for i in c:
            Label(show,text=i[b+1],fg='black').place(x=155,y=m)
            m=m+30
    show=Tk()
    show.title("MY ORDERS")
    show.geometry("500x700")
    ids=StringVar()
    Label(show,width="500", text="MY ORDER", bg="orange",fg="white").pack()
    Label(show,width="500", text=t, bg="orange",fg="white").pack()
    Label(show,text='Cust_id :', bg="orange",fg="white").place(x=105,y=60)
    Entry(show,textvariable=ids,bg="white",justify="center").place(x=205,y=60)
    Button(show, text="<- Back", width=10, height=1, bg="orange",command=uses).place(x=15,y=60)
    Button(show, text="Show", width=10, height=1, bg="orange",command=os).place(x=155,y=100)
    show.mainloop()

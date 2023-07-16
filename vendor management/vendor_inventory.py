from tkinter import *
from  tkinter import  ttk
import  mysql.connector as m
import time
import random
from tkinter import messagebox
db=m.connect(host="localhost",user="root",passwd="12345")
c=db.cursor()
c.execute("create database if not existS pythondata")
c.execute("Use pythondata")
c.execute("create table if not exists products(product_name varchar(30),price varchar(5))")
c.execute("CREATE table if not existS user_au(NAME VARCHAR(30),CONTACT VARCHAR(30),EMAIL VARCHAR(30),PASSWORD VARCHAR(30),GENDER VARCHAR(30),CITY VARCHAR(30),STATE VARCHAR(30))")
c.execute("CREATE table if not existS user_orders(cust_id varchar(10),product_name varchar(30),price varchar(5))")
c.execute("CREATE table if not existS bill(cust_id varchar(10),total varchar(5))")
t=time.asctime(time.localtime(time.time()))
def vendor_i():
    def ai():
        vendor_inv.destroy()
        add()
    def di():
        vendor_inv.destroy()
        delete()
    def ss():
        vendor_inv.destroy()
        sstock()
    def out():
        messagebox.showinfo('Log out','Logged out')
        vendor_inv.destroy()
    def sb():
        vendor_inv.destroy()
        bs()
    vendor_inv=Tk()
    vendor_inv.title("vendor inventory")
    vendor_inv.geometry("400x400")
    Label(vendor_inv,width="400",text="VENDOR INVENTORY",bg='orange',fg='white').pack()
    Label(vendor_inv,width="400",text=t,bg='orange',fg='white').pack()
    Button(vendor_inv,text='Show Stock',width=20,bg='orange',command=ss).place(x=120,y=70)
    Button(vendor_inv,text='add items',width=20,bg='orange',command=ai).place(x=120,y=110)
    Button(vendor_inv,text='delete items',width=20,bg='orange',command=di).place(x=120,y=150)
    Button(vendor_inv,text='show bill',width=20,bg='orange',command=sb).place(x=120,y=190)
    Button(vendor_inv,text='LOG OUT',width=20,bg='orange',command=out).place(x=120,y=260)
    vendor_inv.mainloop()

def delete():
    def bac():
        del_item.destroy()
        vendor_i()
    def addi():
        nams=name.get()
        if nams=='':
            messa.set("Field Empty!!!")
        else:
            qry="delete from products where product_name='"+str(nams)+"'"
            c.execute(qry)
            db.commit()
            messa.set("Data Deleted")
    del_item=Tk()
    del_item.title("DELETE ITEMS")
    del_item.geometry('300x300')
    name=StringVar()
    messa=StringVar()
    Label(del_item,width="300",text="DELETE ITEMS",bg='orange',fg='white').pack()
    Label(del_item,width="300",text=t,bg='orange',fg='white').pack()
    Label(del_item,text='Item Name',bg='orange',fg='white').place(x=115,y=60)
    Label(del_item, text="",textvariable=messa).place(x=115,y=160)
    Entry(del_item,bg="white",justify="center",textvariable=name).place(x=85,y=90)
    Button(del_item,text='DELETE ITEM',width=10,bg='orange',command=addi).place(x=115,y=200)
    Button(del_item,text='<-- BACK',width=10,bg='orange',command=bac).place(x=115,y=230)
    del_item.mainloop()



def add():
    def bac():
        add_item.destroy()
        vendor_i()
    def addi():
        nams=name.get()
        pri=price.get()
        if pri=='' or nams=='':
            messa.set("Field Empty!!!")
        else:
            qry="Insert into products values('"+str(nams)+"','"+str(pri)+"')"
            c.execute(qry)
            db.commit()
            messa.set("Data Inserted")
    add_item=Tk()
    add_item.title("ADD ITEMS")
    add_item.geometry('300x300')
    name=StringVar()
    price=StringVar()
    messa=StringVar()
    Label(add_item,width="300",text="ADD ITEMS",bg='orange',fg='white').pack()
    Label(add_item,width="300",text=t,bg='orange',fg='white').pack()
    Label(add_item,text='Item Name',bg='orange',fg='white').place(x=55,y=60)
    Label(add_item,text='Price',bg='orange',fg='white').place(x=220,y=60)
    Label(add_item, text="",textvariable=messa).place(x=115,y=160)
    Entry(add_item,bg="white",justify="center",textvariable=name).place(x=20,y=90)
    Entry(add_item,bg="white",justify="center",textvariable=price).place(x=170,y=90)
    Button(add_item,text='ADD ITEM',width=10,bg='orange',command=addi).place(x=115,y=200)
    Button(add_item,text='<-- BACK',width=10,bg='orange',command=bac).place(x=115,y=230)
    add_item.mainloop()


def sstock():
    def ba():
        stock.destroy()
        vendor_i()
    stock=Tk()
    stock.title("STOCK")
    stock.geometry('300x600')
    Label(stock,width="300",text="SHOW ITEMS",bg='orange',fg='white').pack()
    Label(stock,width="300",text=t,bg='orange',fg='white').pack()
    Label(stock,text='Item Name',bg='orange',fg='white').place(x=55,y=80)
    Label(stock,text='Price',bg='orange',fg='white').place(x=220,y=80)
    qry="select * from products"
    m=120
    a=-2
    b=-1
    c.execute(qry)
    for i in c:
        Label(stock,text=i[a+2],fg='black').place(x=55,y=m)
        Label(stock,text=i[b+2],fg='black').place(x=220,y=m)
        m=m+30
    Button(stock,text='<-- BACK',width=8,bg='orange',command=ba).place(x=10,y=50)
    stock.mainloop()


def bs():
    def uses():
        show.destroy()
        vendor_i()
    def os():
        odid=ids.get()
        Label(show,text='Customer_id',bg='orange',fg='white').place(x=155,y=160)
        Label(show,text='Total',bg='orange',fg='white').place(x=255,y=160)
        q="select * from bill where cust_id='"+str(odid)+"'"
        c.execute(q)
        m=190
        a=-2
        b=-1
        for i in c:
            Label(show,text=i[a+2],fg='black').place(x=155,y=m)
            Label(show,text=i[b+2],fg='black').place(x=255,y=m)
            m=m+30
    def os1():
        Label(show,text='Customer_id',bg='orange',fg='white').place(x=155,y=160)
        Label(show,text='Total',bg='orange',fg='white').place(x=255,y=160)
        q="select * from bill"
        c.execute(q)
        m=190
        a=-2
        b=-1
        for i in c:
            Label(show,text=i[a+2],fg='black').place(x=155,y=m)
            Label(show,text=i[b+2],fg='black').place(x=255,y=m)
            m=m+30
    show=Tk()
    show.title("BILLS")
    show.geometry("500x700")
    ids=StringVar()
    Label(show,width="500", text="BILLS", bg="orange",fg="white").pack()
    Label(show,width="500", text=t, bg="orange",fg="white").pack()
    Label(show,text='Cust_id :', bg="orange",fg="white").place(x=105,y=60)
    Entry(show,textvariable=ids,bg="white",justify="center").place(x=205,y=60)
    Button(show, text="<- Back", width=10, height=1, bg="orange",command=uses).place(x=15,y=60)
    Button(show, text="Show", width=10, height=1, bg="orange",command=os).place(x=95,y=100)
    Button(show, text="Show All", width=10, height=1, bg="orange",command=os1).place(x=205,y=100)
    show.mainloop()


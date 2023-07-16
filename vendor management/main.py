from tkinter import *
from  tkinter import  ttk
import  mysql.connector as m
import time
import random
import user_authentication1 as u
t=time.asctime(time.localtime(time.time()))
import vendor_authentication as v
def programs():
    def dest():
        program.destroy()
        v.reg()
    def cu():
        program.destroy()
        u.reg()
    program=Tk()
    program.title("User Authentication")
    program.geometry("200x200")
    Label(program,width="200",text="VENDOR MANAGEMENT SYSTEM",bg='orange',fg='white').pack()
    Button(program,text='Login as Vendor',width=20,bg='orange',command=dest).place(x=30,y=40)
    Button(program,text='Login as Customer',width=20,bg='orange',command=cu).place(x=30,y=110)
    program.mainloop()
programs()

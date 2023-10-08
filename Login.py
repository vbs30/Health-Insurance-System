from tkinter import *
from tkinter import messagebox

import mysql.connector

frame = Tk()

frame.geometry("1000x750")
frame.title("Health Insurance Management System")
frame.config(bg='white')
f1 = Frame(frame)

def click():
    frame.destroy()
    import new
'''
def mainPageClick():
    frame.destroy()
    if e1.get() == "username" or e2.get() == "password":
        messagebox.showerror("Error", "Enter User Name And Password")
    else:
        try:
            con = mysql.connect(host="localhost", user="root", password="yutika@14",port="3308", database="healthinsurance")
            cur = con.cursor()
            cur.execute("select * from sign where username=%s and password = %s",
                        (e1.get(), e2.get()))
            row = cur.fetchone()
            if row == None:
                messagebox.showerror("Error", "Invalid User Name And Password")
            else:
                messagebox.showinfo("Success", "Successfully Login")
                #close()
                #deshboard()
            con.close()
        except Exception as es:
            messagebox.showerror("Error")
    import Category
'''
def mainPageClick():
    mydb = mysql.connector.connect(host='localhost', user='root', password='Vinayak@2002', port='3306', database='signup')
    mycursor = mydb.cursor()
    username = e1.get()
    password = e2.get()

    y = ("select * from sign where username=%s and password=%s")
    mycursor.execute(y,[(username),(password)])
    result = mycursor.fetchall()
    if result:
        messagebox.showinfo("","Login successful.")
        frame.destroy()
        import Mainpage
    else:
        messagebox.showerror('error','login fail')

photo2 = PhotoImage(file='loginnew.png')
labelph2 = Label(frame, image = photo2).place(x=0, y=0)
photo = PhotoImage(file='locked .png')
labelph = Label(frame,image = photo,bg='grey85').place(x=475, y=155)
photo1 = PhotoImage(file='user.png')
labelph1 = Label(labelph2, image = photo1, bg='grey85').place(x=475, y=275)

l1 = Label(frame,text="Username",font=('Times New Roman',20,'bold'),bg='grey85',fg='grey2').place(x=525,y=150)
e1 = Entry(frame,font=('Times New Roman',18,'bold'),bg="grey90")
e1.place(x=690,y=150)
l2 = Label(frame,text="Password",font=('Times New Roman',20,'bold'),bg='grey85',fg='grey2').place(x=525,y=270)
e2 = Entry(frame,show='*',font=('Times New Roman',18,'bold'),bg='grey90')
e2.place(x=690,y=270)

b1=Button(frame,text="Login",font=('Times New Roman',20,'bold'),padx=25,pady=7,bg='pale green',fg='maroon',command=mainPageClick).place(x=550,y=460)
b2=Button(frame,text="Signup",font=('Times New Roman',20,'bold'),padx=25,pady=7,bg='pale green',fg='maroon',command = click).place(x=790,y=460)

frame.mainloop()
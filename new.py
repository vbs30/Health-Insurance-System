from tkinter import *
from tkinter import messagebox

import mysql.connector


def LoginPage():
    frame1.destroy()
    import Login


def MyClick():
    if N1.get() == "" or P1.get() == "" or A1.get() == "" or U1.get() == "" or P2.get() == "":
        messagebox.showerror('error', 'Enter all the fields')
    else:
        db = mysql.connector.connect(host='localhost', user='root', password='Vinayak@2002', port='3306', database='signup')
        mycursor = db.cursor()
        mycursor.execute("INSERT INTO `Sg` (Name, Phone_number,Age, USERNAME, PASSWORD) VALUES(%s, %s, %s, %s, %s)",
                     (str(Name1.get()), str(Phone.get()), str(Age1.get()), str(User.get()), str(Pass.get())))
        db.commit()


"""
def clicked(value):
    db = mysql.connector.connect(host='localhost', user='root', password='Vinayak@2002', port='3306', database='signup')
    mycursor = db.cursor()
    mycursor.execute("INSERT INTO `Sg` (gender) VALUES(?)", (r.get(),))
    db.commit()
"""''

frame1 = Tk()
frame1.title("SignUp Page")
frame1.geometry("900x750")
frame1.config(bg='floral white')

Name1 = StringVar()
Phone = StringVar()
Age1 = StringVar()
User = StringVar()
Pass = StringVar()

Name = Label(frame1, text="Name", bg='floral white',font=("Times New Roman", 18)).place(x=250, y=70)
N1 = Entry(frame1, font=2, textvariable=Name1)
N1.place(x=450, y=70)
Phone_number = Label(frame1, text="Phone number", font=("Times New Roman", 17), bg='floral white').place(x=250, y=150)
P1 = Entry(frame1, font=2, textvariable=Phone)
P1.place(x=450, y=150)
Age = Label(frame1, text="Age", font=("Times New Roman", 18), bg='floral white').place(x=250, y=230)
A1 = Entry(frame1, font=2, textvariable=Age1)
A1.place(x=450, y=230)
Username = Label(frame1, text="Username", font=("Times New Roman", 18), bg='floral white').place(x=250, y=310)
U1 = Entry(frame1, font=2, textvariable=User)
U1.place(x=450, y=310)
Password = Label(frame1, text="Password", font=("Times New Roman", 18), bg='floral white').place(x=250, y=390)
P2 = Entry(frame1, font=2, textvariable=Pass)
P2.place(x=450, y=390)
Gender = Label(frame1, text="Gender", font=("Times New Roman", 18), bg='floral white').place(x=250, y=470)
#G1 = Entry(frame1, font=2).place(x=450, y=470)




r = StringVar()
R1 = Radiobutton(frame1,text='Male',variable=r,value=1,font=("Times New Roman",18),bg='floral white')
R1.place(x=450,y=470)
R2 = Radiobutton(frame1,text='Female',variable=r,value=2,font=("Times New Roman",19),bg='floral white')
R2.place(x=600,y=470)


signup1 = Button(frame1, text="SignUp", font=0, padx=25,bg='pale green', pady=7,command=MyClick).place(x=250, y=600)
cancel1 = Button(frame1, text="Cancel", font=0, padx=25, pady=7, bg='pale green',command=LoginPage).place(x=540, y=600)


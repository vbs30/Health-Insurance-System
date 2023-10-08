from tkinter import *
from tkinter import messagebox

import mysql.connector

root = Tk()
root.geometry("1000x800")
root.config(bg='white')
root.title("Health Insurance Management System")

photo2 = PhotoImage(file='formborder1.png')
labelph2 = Label(root, image = photo2).place(x=0, y=0)


def click1():
    root.destroy()
    import Mainpage


def click():
    if N1.get()=='' or P1.get()=='' or A1.get()=='' or U1.get()=='' or P2.get()=='' or P3.get()=='' or P4.get()=='' or E1.get()=='' or A2.get()=='':
        messagebox.showerror('error', 'login fail')
    else:
        db = mysql.connector.connect(host='localhost', user='root', password='Vinayak@2002', port='3306',database='signup')
        mycursor = db.cursor()
        mycursor.execute("INSERT INTO `personaldet` VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                     (str(N1.get()), str(P1.get()), str(A1.get()), str(U1.get()), str(P2.get()),str(P3.get()),str(E1.get()),str(A2.get()),str(P4.get())))
        db.commit()
        root.destroy()
        import form2


Personal_det = Label(root, text="Personal Details", bg='white',font=("Times New Roman", 22, 'bold')).place(x=370, y=10)

Name = Label(root, text="Name", bg='white', fg="Navy blue", font=("Times New Roman", 18)).place(x=60, y=90)
N1 = Entry(root, font=2, bg='Grey94')
N1.place(x=210, y=90)
Phone_number = Label(root, text="DOB", fg="Navy blue", font=("Times New Roman", 17), bg='white').place(x=570, y=90)
P1 = Entry(root, font=2, bg='Grey94')
P1.place(x=680, y=90)

Occupation = Label(root, text="Occupation", fg="crimson", font=("Times New Roman", 18), bg='white').place(x=60, y=190)
A1 = Entry(root, font=2, bg='Grey94')
A1.place(x=210, y=190)
Annual_income = Label(root, text="Income", fg="crimson", font=("Times New Roman", 18), bg='white').place(x=570, y=190)
U1 = Entry(root, font=2, bg='Grey94')
U1.place(x=680, y=190)

Address = Label(root, text="Address", fg="Navy blue", font=("Times New Roman", 18), bg='white').place(x=60, y=290)
P2 = Entry(root, font=2, width=50, bg='Grey94')
P2.place(x=210, y=290)

Phone = Label(root, text="Mobile", fg="crimson", font=("Times New Roman", 18), bg='white').place(x=60, y=390)
P3 = Entry(root, font=2, bg='Grey94')
P3.place(x=210, y=390)
Email = Label(root, text="Email id", fg="crimson", font=("Times New Roman", 18), bg='white').place(x=570, y=390)
E1 = Entry(root, font=2, bg='Grey94')
E1.place(x=680, y=390)

Aadhar = Label(root, text="Aadhar number", fg="Navy blue", font=("Times New Roman", 18), bg='white').place(x=60, y=490)
A2 = Entry(root, font=2, width=30, bg='Grey94')
A2.place(x=250, y=490)

Pan = Label(root, text="PAN number", fg="crimson", font=("Times New Roman", 18), bg='white').place(x=60, y=590)
P4 = Entry(root, font=2, width=30, bg='Grey94')
P4.place(x=250, y=590)

photo = PhotoImage(file = "next (1).png")
b1 = Button(root,text="", font=0, padx=50, pady=10,command=click, image=photo).place(x=870, y=670)

photo1 = PhotoImage(file = "Back.png")
b2 = Button(root,text="", font=0, padx=50, pady=10,command=click1, image=photo1).place(x=80, y=670)

# Gender = Label(root, text="Gender", font=("Times New Roman", 18), bg='white').place(x=50, y=470)
# r = StringVar()
# R1 = Radiobutton(root,text='Male',variable=r,value=1,font=("Times New Roman",18),bg='White').place(x=450,y=470)
# R2 = Radiobutton(root,text='Female',variable=r,value=2,font=("Times New Roman",19),bg='White').place(x=600,y=470)

root.mainloop()
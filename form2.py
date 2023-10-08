from tkinter import *
from tkinter import ttk, messagebox
import tk as tk
import mysql.connector

def click2():
    root.destroy()
    import Form


def click():
    if N1.get()=='' or P1.get()=='' or A1.get()=='' or U1.get()=='' or P2.get()=='':
        messagebox.showerror('error', 'login fail')
    else:
        db = mysql.connector.connect(host='localhost', user='root', password='Vinayak@2002', port='3306',database='signup')
        mycursor = db.cursor()
        mycursor.execute("INSERT INTO `nominee` VALUES(%s, %s, %s, %s, %s)",
                     (str(N1.get()), str(P1.get()), str(A1.get()), str(U1.get()), str(P2.get())))
        db.commit()
        root.destroy()
        import form3

root = Tk()
root.geometry("1000x800")
root.config(bg='white')
root.title("Health Insurance Management System")
photo2 = PhotoImage(file='formborder1.png')
labelph2 = Label(root, image = photo2).place(x=0, y=0)

Nominee_det = Label(root, text="Nominee Details", bg='white',font=("Times New Roman", 20, 'bold')).place(x=400, y=10)

Name = Label(root, text="Nominee's Name", bg='white',fg='SpringGreen4',font=("Times New Roman", 18)).place(x=80, y=90)
N1 = Entry(root, font=2, bg='Grey94')
N1.place(x=370, y=90)
Phone_number = Label(root, text="Relationship to proposer",fg='maroon', font=("Times New Roman", 17), bg='white').place(x=80, y=180)
P1 = Entry(root, font=2, bg='Grey94')
P1.place(x=370, y=180)

DOB = Label(root, text="DOB",fg='SpringGreen4', font=("Times New Roman", 18), bg='white').place(x=80, y=280)
A1 = Entry(root, font=2, bg='Grey94')
A1.place(x=370, y=280)
Age = Label(root, text="Age",fg='maroon', font=("Times New Roman", 18), bg='white').place(x=80, y=380)
U1 = Entry(root, font=2, bg='Grey94')
U1.place(x=370, y=380)

Policy = Label(root, text="Policy name",fg='SpringGreen4', font=("Times New Roman", 18), bg='white').place(x=80, y=470)
n = StringVar()
P2 = ttk.Combobox(root, width=30,textvariable=n)
P2['values'] = ('Active assure Diamond with super NCB','Optima Restore','Maxhealth Campanion','Comprehensive individual','Young star individual silver','Early cover')
#P2.grid(column=100, row=500)
P2.place(x=380,y=470)
P2.current()

photo = PhotoImage(file = "next (1).png")
b1 = Button(root,text="", font=0, padx=50, pady=10, image=photo,command=click).place(x=870, y=650)
photo1 = PhotoImage(file = "Back.png")
b2 = Button(root,text="", font=0, padx=50, pady=10,command=click2, image=photo1).place(x=80, y=670)

root.mainloop()

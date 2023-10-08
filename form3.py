from tkinter import *
import mysql.connector

root = Tk()
root.geometry("1000x800")
root.config(bg='white')
root.title("Health Insurance Management System")
photo2 = PhotoImage(file='formborder1.png')
labelph2 = Label(root, image = photo2).place(x=0, y=0)

def click():

        db = mysql.connector.connect(host='localhost', user='root', password='Vinayak@2002', port='3306',database='signup')
        mycursor = db.cursor()
        mycursor.execute("INSERT INTO `bankdetails` VALUES(%s, %s, %s, %s)",
                     (str(N1.get()), str(P1.get()), str(A1.get()), str(U1.get())))
        # db.commit()
        root.destroy()
        import form2


def click1():
    root.destroy()
    import Mainpage


Bank_det = Label(root, text="Bank Details", bg='white',font=("Times New Roman", 20, 'bold')).place(x=400, y=10)

Name = Label(root, text="Account Number", bg='white',fg='dark magenta',font=("Times New Roman", 18)).place(x=80, y=80)
N1 = Entry(root, font=2, bg='Grey94')
N1.place(x=370, y=80)
Phone_number = Label(root, text="Name of bank",fg='orange red', font=("Times New Roman", 17), bg='white').place(x=80, y=170)
P1 = Entry(root, font=2, bg='Grey94')
P1.place(x=370, y=170)

DOB = Label(root, text="Name of branch",fg='dark magenta', font=("Times New Roman", 18), bg='white').place(x=80, y=270)
A1 = Entry(root, font=2, bg='Grey94')
A1.place(x=370, y=270)
Age = Label(root, text="IFSC code",fg='orange red', font=("Times New Roman", 18), bg='white').place(x=80, y=370)
U1 = Entry(root, font=2, bg='Grey94')
U1.place(x=370, y=370)
type = Label(root, text="Type of account",fg='dark magenta', font=("Times New Roman", 18), bg='white').place(x=80, y=470)
r = StringVar()
R1 = Radiobutton(root,text='Saving account',variable=r,value=1,font=("Times New Roman",18),bg='White').place(x=370,y=470)
R2 = Radiobutton(root,text='Current account',variable=r,value=2,font=("Times New Roman",19),bg='White').place(x=620,y=470)

photo = PhotoImage(file = "next (1).png")
b1 = Button(root,text="", font=0, padx=50, pady=10, image=photo,command=click).place(x=870, y=650)
photo1 = PhotoImage(file = "Back.png")
b2 = Button(root,text="", font=0, padx=50, pady=10,command=click1, image=photo1).place(x=80, y=670)


root.mainloop()
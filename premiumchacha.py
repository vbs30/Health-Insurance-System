from tkinter import *
import mysql.connector

root = Tk()
root.geometry('1000x800')
root.config(bg='floral white')
root.title("Health Insurance Management System")

def calculate():
    db = mysql.connector.connect(host='localhost', user='root', password='Vinayak@2002', port='3306', database='signup')
    mycursor = db.cursor()
    premium = int(e1.get())
    if clicked1.get()=='18-29':
        npremium = int(premium*1.1)
        e2.insert(0, npremium)
        n12premium = npremium*12
        e3.insert(0, n12premium)
        e4.insert(0, npremium * 3)

    elif clicked1.get()=='30-45':
        npremium = int(premium*1.2)
        e2.insert(0, npremium)
        n12premium = npremium*12
        e3.insert(0, n12premium)
        e4.insert(0, npremium * 3)

    elif clicked1.get()=='45-59':
        npremium = int(premium*1.3)
        e2.insert(0, npremium)
        n12premium = npremium*12
        e3.insert(0, n12premium)
        e4.insert(0, npremium * 3)

    elif clicked1.get()=='60+':
        npremium = int(premium*1.4)
        e2.insert(0, npremium)
        n12premium = npremium*12
        e3.insert(0, n12premium)
        e4.insert(0, npremium*3)


def clear():

    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)

label = Label(root, text="Premium Calculator", bg='floral white', fg='Red', font=('Times New Roman', 22, 'bold')).place(x=400, y=10)

label1 = Label(root, text="Insurance Type", bg='floral white', fg='navy blue', font=('Times New Roman', 18)).place(x=90, y=90)
label2 = Label(root, text="Product", bg='floral white', fg='Orange red', font=('Times New Roman', 18)).place(x=530, y=90)
label3 = Label(root, text="Your age", bg='floral white', fg='Orange red', font=('Times New Roman', 18)).place(x=130, y=210)
label4 = Label(root, text="Starting Amount", bg='floral white', fg='navy blue', font=('Times New Roman', 18)).place(x=530, y=210)

label5 = Label(root, text="Premium amount", bg='floral white', fg='Darkviolet', font=('Times New Roman', 18)).place(x=250, y=460)
label6 = Label(root, text="Annual premium", bg='floral white', fg='Darkviolet', font=('Times New Roman', 18)).place(x=250, y=520)
label7 = Label(root, text="Quarterly premium", bg='floral white', fg='Darkviolet', font=('Times New Roman', 18)).place(x=250, y=580)


clicked8 = StringVar()
clicked8.set('Select')
drop2 = OptionMenu(root,clicked8, 'Individual Insurance', 'Family Insurance', 'Critical illness', 'Senior Citizen', 'Mediclaim', 'Accidental cover')
drop2.place(x=290, y=90)
drop2.config(width=15)

clicked = StringVar()
clicked.set('Select')
drop = OptionMenu(root,clicked, 'Active assure Diamond with super NCB', 'Optima Restore', 'Maxhealth Campanion', 'Comprehensive individual', 'Young star individual silver', 'Early cover')
drop.place(x=670, y=90)
drop.config(width=15)

clicked1 = StringVar()
clicked1.set("Select ")
drop11 = OptionMenu(root, clicked1, '18-29', '30-45', '45-59', '60+')
drop11.place(x=290, y=210)
drop11.config(width=15)

e1 = Entry(root,font=2,width=15, bg='Grey94')
e1.place(x=720,y=210)

e2 = Entry(root,font=2,width=15, bg='Grey94')
e2.place(x=550,y=460)
e3 = Entry(root,font=2,width=15, bg='Grey94')
e3.place(x=550,y=520)
e4 = Entry(root,font=2,width=15, bg='Grey94')
e4.place(x=550,y=580)



cancel2 = Button(root, text="Calculate Premium", bg='black',fg='white', font=('Times New Roman',18,'bold'), padx=40, pady=10, command=calculate)
cancel2.place(x=120, y=320)
Clear = Button(root, text="Clear", bg='black',fg='white',font=('Times New Roman',18,'bold'), padx=40, pady=10, command=clear)
Clear.place(x=600, y=320)

root.mainloop()

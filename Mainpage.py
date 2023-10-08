from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector

root = Tk()
root.geometry("1200x900")
root.title("Health Insurance Management System")
photo2 = PhotoImage(file='pnn (1).png')
labelph2 = Label(root, image = photo2).place(x=0, y=0)
showoff1 = Label(root, text="Your Health, Our Promise !", bg='white', font=('Segoe script', 30, 'bold'),fg='medium orchid4')
showoff1.place(x=380, y=40)


def click2():
    root.destroy()
    import Form


def click3():
    root.destroy()
    import premiumchacha


def click1():
    my_game.place_forget()
    b1.place_forget()
    b2.place_forget()
    cancel1.place(x=340, y=720)
    cancel2.place(x=640, y=720)
    l2.place(x=150, y=420)
    l4.place(x=150, y=190)
    l5.place(x=150, y=310)
    drop.place(x=400, y=420)
    drop1.place(x=400, y=190)
    drop2.place(x=400, y=310)

my_game = ttk.Treeview(root, height=26)
b1 = Button(root, text="Apply Scheme", font=('Times New Roman',18,'bold'), padx=50, bg='aquamarine', pady=10, command=click2)
b2 = Button(root, text="Cancel", font=('Times New Roman',18,'bold'), bg='aquamarine', padx=50, pady=10, command=click1)

def tableview():
    db = mysql.connector.connect(host='localhost', user='root', password='Vinayak@2002', port='3306', database='signup')
    mycursor = db.cursor()
    cancel1.place_forget()
    cancel2.place_forget()
    l2.place_forget()
    l4.place_forget()
    l5.place_forget()
    drop.place_forget()
    drop1.place_forget()
    drop2.place_forget()
    label2.place_forget()
    label3.place_forget()
    label4.place_forget()
    label5.place_forget()
    drop11.place_forget()
    drop12.place_forget()
    drop13.place_forget()
    label6.place_forget()
    label7.place_forget()
    label8.place_forget()
    drop14.place_forget()
    drop15.place_forget()
    label1.place_forget()
    dropx.place_forget()
    b1.place(x=300,y=700)
    b2.place(x=700, y=700)

    my_game['columns'] = ('Insurance Company', 'Product', 'Cover', 'Starting at')
    my_game.column("#0", width=0, stretch=NO)
    my_game.column("Insurance Company", width=290)
    my_game.column("Product", width=290)
    my_game.column("Cover", width=170, anchor=CENTER)
    my_game.column("Starting at", width=170, anchor=CENTER)

    my_game.heading("#0", text="", anchor=CENTER)
    my_game.heading("Insurance Company", text="Insurance Company", anchor=CENTER)
    my_game.heading("Product", text="Product", anchor=CENTER)
    my_game.heading("Cover", text="Cover", anchor=CENTER)
    my_game.heading("Starting at", text="Starting at", anchor=CENTER)

    my_game.place(x=145, y=140)

    if clicked8.get() == 'Individual Insurance' and clicked7.get()=='5 Lac':
        user = mycursor.execute("Select Insurance_Company,Product,Cover,Starting_at from insur where cover='5 Lac' and type='Individual'")
        count = 0
        for t in mycursor:
            my_game.insert('', index=count, text='', values=(t[0], t[1], t[2], t[3]))
            count = count + 1

    elif clicked8.get() == 'Individual Insurance' and clicked7.get()=='10 Lac':
        user = mycursor.execute("Select Insurance_Company,Product,Cover,Starting_at from insur where cover='10 Lac' and type='Individual'")
        count = 0
        for a in mycursor:
            my_game.insert('', index=count, text='', values=(a[0], a[1], a[2], a[3]))
            count = count + 1

    elif clicked8.get() == 'Family Insurance' and clicked7.get()=='5 Lac':
        user = mycursor.execute("Select Insurance_Company,Product,Cover,Starting_at from insur where cover='5 Lac' and type='Family'")
        count = 0
        for b in mycursor:
            my_game.insert('', index=count, text='', values=(b[0], b[1], b[2], b[3]))
            count = count + 1

    elif clicked8.get() == 'Family Insurance' and clicked7.get()=='10 Lac':
        user = mycursor.execute("Select Insurance_Company,Product,Cover,Starting_at from insur where cover='10 Lac' and type='Family'")
        count = 0
        for c in mycursor:
            my_game.insert('', index=count, text='', values=(c[0], c[1], c[2], c[3]))
            count = count + 1

    elif clicked8.get() == 'Critical illness' and clicked7.get()=='5 Lac':
        user = mycursor.execute("Select Insurance_Company,Product,Cover,Starting_at from insur where cover='5 Lac' and type='Critical'")
        count = 0
        for d in mycursor:
            my_game.insert('', index=count, text='', values=(d[0], d[1], d[2], d[3]))
            count = count + 1

    elif clicked8.get() == 'Senior Citizen' and clicked7.get()=='5 Lac':
        user = mycursor.execute("Select Insurance_Company,Product,Cover,Starting_at from insur where cover='5 Lac' and type='Senior'")
        count = 0
        for e in mycursor:
            my_game.insert('', index=count, text='', values=(e[0], e[1], e[2], e[3]))
            count = count + 1

    elif clicked8.get() == 'Mediclaim' and clicked7.get()=='5 Lac':
        user = mycursor.execute("Select Insurance_Company,Product,Cover,Starting_at from insur where cover='5 Lac' and type='Mediclaim'")
        count = 0
        for f in mycursor:
            my_game.insert('', index=count, text='', values=(f[0], f[1], f[2], f[3]))
            count = count + 1

    elif clicked8.get() == 'Accidental cover' and clicked7.get()=='5 Lac':
        user = mycursor.execute("Select Insurance_Company,Product,Cover,Starting_at from insur where cover='5 Lac' and type='Accident'")
        count = 0
        for g in mycursor:
            my_game.insert('', index=count, text='', values=(g[0], g[1], g[2], g[3]))
            count = count + 1


"""
def click():
    if clicked6.get() == 'Category' or clicked7.get() == 'Coverage' or clicked8.get() == 'Insurance':
        messagebox.showerror("error", "error")

    else:
        if clicked6.get() == 'Myself':
            if clickedx.get() == 'Select age':
                messagebox.showerror("error", "error")
            else:
                root.destroy()

        elif clicked6.get() == 'My Family':
            if clicked1.get() == 'Select' or clicked2.get() == 'Select' or clicked3.get() == 'Select':
                messagebox.showerror("error", "error")
            else:
                root.destroy()

        elif clicked6.get() == 'My Parents':
            if clicked4.get() == 'Select' or clicked5.get() == 'Select':
                messagebox.showerror("error", "error")
            else:
                root.destroy()
"""

def myself(clicked):

    if clicked == 'Myself':
        label1.place(x=280, y=520)

        dropx.place(x=450, y=520)

        label2.place_forget()
        label3.place_forget()
        label4.place_forget()
        label5.place_forget()
        drop11.place_forget()
        drop12.place_forget()
        drop13.place_forget()

        label6.place_forget()
        label7.place_forget()
        label8.place_forget()
        drop14.place_forget()
        drop15.place_forget()

    elif clicked == 'My Family':
        label2.place(x=280, y=520)
        label3.place(x=280, y=590)
        label4.place(x=700, y=590)
        label5.place(x=280, y=650)

        drop11.place(x=520, y=590)
        drop12.place(x=830, y=590)
        drop13.place(x=520, y=650)

        label1.place_forget()
        dropx.place_forget()

        label6.place_forget()
        label7.place_forget()
        label8.place_forget()
        drop14.place_forget()
        drop15.place_forget()

    elif clicked == 'My Parents':

        label6.place(x=280, y=520)
        label7.place(x=280, y=590)
        label8.place(x=600, y=590)

        drop14.place(x=420, y=590)
        drop15.place(x=750, y=590)

        label1.place_forget()
        dropx.place_forget()

        label2.place_forget()
        label3.place_forget()
        label4.place_forget()
        label5.place_forget()
        drop11.place_forget()
        drop12.place_forget()
        drop13.place_forget()


#myself
label1 = Label(root, text="Your Age", bg='floral white', fg='Darkviolet', font=('Times New Roman', 18))
clickedx = StringVar()
clickedx.set("Select age")
dropx = OptionMenu(root, clickedx, '18-29', '30-45', '45-59', '60+')
dropx.config(width=13)

# my_family
label2 = Label(root, text="Select age of all members", bg='floral white', fg='saddle brown', font=('Times New Roman', 18))
label3 = Label(root, text="You", bg='floral white', fg='Darkviolet', font=('Times New Roman', 18))
label4 = Label(root, text="Spouse", bg='floral white', fg='Darkviolet', font=('Times New Roman', 18))
label5 = Label(root, text="Number of children", bg='floral white', fg='Darkgreen', font=('Times New Roman', 18))

clicked1 = StringVar()
clicked1.set("Select ")
drop11 = OptionMenu(root, clicked1, '18-29', '30-45', '45-59', '60+')
clicked2 = StringVar()
clicked2.set("Select ")
drop12 = OptionMenu(root, clicked2, '18-29', '30-45', '45-59', '60+')
clicked3 = StringVar()
clicked3.set("Select")
drop13 = OptionMenu(root, clicked3, '1', '2', '3', '4')

# my_parents
label6 = Label(root, text="Select age of all members", bg='floral white',fg='saddle brown',font=('Times New Roman', 18))
label7 = Label(root, text="Father", bg='floral white', fg='red', font=('Times New Roman', 18))
label8 = Label(root, text="Mother", bg='floral white', fg='red', font=('Times New Roman', 18))
clicked4 = StringVar()
clicked4.set("Select")
drop14 = OptionMenu(root, clicked4, '45-59', '60-75', '75-99')
clicked5 = StringVar()
clicked5.set("Select")
drop15 = OptionMenu(root, clicked5, '45-59', '60-75', '75-99')

clicked6 = StringVar()
clicked6.set('Category')
drop = OptionMenu(root,clicked6, 'Myself', 'My Family', 'My Parents',command=myself)
drop.place(x=440, y=420)
drop.config(width=20)

clicked7 = StringVar()
clicked7.set('Coverage')
drop1 = OptionMenu(root, clicked7, '5 Lac', '10 Lac', '25 Lac', '50 Lac', '1 Cr')
drop1.place(x=440, y=190)
drop1.config(width=20)

clicked8 = StringVar()
clicked8.set('Insurance')
drop2 = OptionMenu(root,clicked8, 'Individual Insurance', 'Family Insurance', 'Critical illness', 'Senior Citizen', 'Mediclaim', 'Accidental cover')
drop2.place(x=440, y=310)
drop2.config(width=20)

l2 = Label(root, text='Category', bg='Floral white', fg='blue', font=("Times New Roman", 19, 'bold'))
l2.place(x=150, y=420)
l4 = Label(root, text='Coverage', bg='Floral white', fg='red', font=("Times New Roman", 19, 'bold'))
l4.place(x=150, y=190)
l5 = Label(root, text='Types of insurance', bg='Floral white', fg='blue', font=('Times New Roman', 18, 'bold'))
l5.place(x=150, y=310)

cancel1 = Button(root, text="Display", bg='medium spring green', font=('Times New Roman',18,'bold'), padx=40, pady=10,command=tableview)
cancel1.place(x=340, y=720)
cancel2 = Button(root, text="Calculate Premium", bg='medium spring green', font=('Times New Roman',18,'bold'), padx=40, pady=10,command=click3)
cancel2.place(x=640, y=720)

style = ttk.Style()
style.theme_use('default')
#style.configure("Treeview", background='light blue1', foreground='red', fieldbackground='light blue1')
style.map("Treeview", background=[('selected', '#327083')])

root.mainloop()
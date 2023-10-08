from tkinter import *
from tkinter import messagebox
import mysql.connector

import mysql.connector

root = Tk()
root.geometry("1200x800")
root.title("Health Insurance Management System")
root.config(bg='white')

def click():
    db = mysql.connector.connect(host='localhost', user='root', password='Vinayak@2002', port='3306',
                                 database='signup')
    mycursor = db.cursor()
    mycursor.execute("INSERT INTO `person1` VALUES(%s, %s, %s, %s, %s, %s, %s)",
                     (str(e1.get()), str(f1.get()), str(g1.get()), str(h1.get()),str(i1.get()),str(k1.get()),str(y1.get())))
    mycursor.execute("INSERT INTO `person2` VALUES(%s, %s, %s, %s, %s, %s, %s)",
                     (str(e2.get()), str(f2.get()), str(g2.get()), str(h2.get()), str(i2.get()), str(k2.get()),
                      str(y2.get())))
    mycursor.execute("INSERT INTO `person3` VALUES(%s, %s, %s, %s, %s, %s, %s)",
                     (str(e3.get()), str(f3.get()), str(g3.get()), str(h3.get()), str(i3.get()), str(k3.get()),
                      str(y3.get())))
    mycursor.execute("INSERT INTO `person4` VALUES(%s, %s, %s, %s, %s, %s, %s)",
                     (str(e4.get()), str(f4.get()), str(g4.get()), str(h4.get()), str(i4.get()), str(k4.get()),
                      str(y4.get())))
    db.commit()
    root.destroy()
    messagebox.showinfo('','Submitted')


label = Label(root,text="Has the person proposed for insurance ever suffered or suffering from any of the following: ",font=("Times New Roman", 22, 'bold'),bg='white').place(x=10,y=10)

l1 = Label(root,text="Heart Disease, Peripheral Vascular Disease",fg='saddle brown',font=("Times New Roman", 18),bg='white').place(x=60,y=110)
e1 = Entry(root,font=2,width=3, bg='Grey94')
e1.place(x=850,y=110)
e2 = Entry(root,font=2,width=3, bg='Grey94')
e2.place(x=930,y=110)
e3 = Entry(root,font=2,width=3, bg='Grey94')
e3.place(x=1010,y=110)
e4 = Entry(root,font=2,width=3, bg='Grey94')
e4.place(x=1090,y=110)

l2 = Label(root,text="Diabetes, High blood pressure, High Cholesterol",fg='blue',font=("Times New Roman", 18),bg='white').place(x=60,y=180)
f1 = Entry(root,font=2,width=3, bg='Grey94')
f1.place(x=850,y=180)
f2 = Entry(root,font=2,width=3, bg='Grey94')
f2.place(x=930,y=180)
f3 = Entry(root,font=2,width=3, bg='Grey94')
f3.place(x=1010,y=180)
f4 = Entry(root,font=2,width=3, bg='Grey94')
f4.place(x=1090,y=180)

l3 = Label(root,text="Tuberculosis (TB), any Respiraton / Lung disease",fg='saddle brown',font=("Times New Roman", 18),bg='white').place(x=60,y=250)
g1 = Entry(root,font=2,width=3, bg='Grey94')
g1.place(x=850,y=250)
g2 = Entry(root,font=2,width=3, bg='Grey94')
g2.place(x=930,y=250)
g3 = Entry(root,font=2,width=3, bg='Grey94')
g3.place(x=1010,y=250)
g4 = Entry(root,font=2,width=3, bg='Grey94')
g4.place(x=1090,y=250)

l4 = Label(root,text="Disease of Eye, Ear, Nose, Throat, Thyroid ",fg='blue',font=("Times New Roman", 18),bg='white').place(x=60,y=320)
h1 = Entry(root,font=2,width=3, bg='Grey94')
h1.place(x=850,y=320)
h2 = Entry(root,font=2,width=3, bg='Grey94')
h2.place(x=930,y=320)
h3 = Entry(root,font=2,width=3, bg='Grey94')
h3.place(x=1010,y=320)
h4 = Entry(root,font=2,width=3, bg='Grey94')
h4.place(x=1090,y=320)

l5 = Label(root,text="Cancer, Tumour, lump, cyst, ulcer ",fg='saddle brown',font=("Times New Roman", 18),bg='white').place(x=60,y=390)
i1 = Entry(root,font=2,width=3, bg='Grey94')
i1.place(x=850,y=390)
i2 = Entry(root,font=2,width=3, bg='Grey94')
i2.place(x=930,y=390)
i3 = Entry(root,font=2,width=3, bg='Grey94')
i3.place(x=1010,y=390)
i4 = Entry(root,font=2,width=3, bg='Grey94')
i4.place(x=1090,y=390)

l7 = Label(root,text="Disease of Stomach, Intestine, Liver, Gall bladder / Pancreas, ",fg='blue',font=("Times New Roman", 18),bg='white').place(x=60,y=460)
l8 = Label(root,text="Kidney, Urinary bladder, Urinary Tract Diseases ",fg='blue',font=("Times New Roman", 18),bg='white').place(x=60,y=490)
k1 = Entry(root,font=2,width=3, bg='Grey94')
k1.place(x=850,y=460)
k2 = Entry(root,font=2,width=3, bg='Grey94')
k2.place(x=930,y=460)
k3 = Entry(root,font=2,width=3, bg='Grey94')
k3.place(x=1010,y=460)
k4 = Entry(root,font=2,width=3, bg='Grey94')
k4.place(x=1090,y=460)

l9 = Label(root,text="Does the person purposed for insurance chew tobacco, smoke, consume alcohol ",fg='saddle brown',font=("Times New Roman", 18),bg='white').place(x=60,y=560)
y1 = Entry(root,font=2,width=3, bg='Grey94')
y1.place(x=850,y=560)
y2 = Entry(root,font=2,width=3, bg='Grey94')
y2.place(x=930,y=560)
y3 = Entry(root,font=2,width=3, bg='Grey94')
y3.place(x=1010,y=560)
y4 = Entry(root,font=2,width=3, bg='Grey94')
y4.place(x=1090,y=560)

b = Button(root, text="Submit", bg='pale green', font=0, padx=25, pady=7,command=click).place(x=500, y=650)

root.mainloop()
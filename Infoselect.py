from tkinter import *
import tkinter as tk

root = Tk()
root.title("Health Insurance Management System")
root.geometry("1000x800")


def click1():
    root.destroy()
    import Info


def click2():
    root.destroy()
    import Info1


def click3():
    root.destroy()
    import Info2


def click4():
    root.destroy()
    import Info3


def click5():
    root.destroy()
    import Info4


def click6():
    root.destroy()
    import Info5


def click7():
    root.destroy()
    import firstpage


photo1 = PhotoImage(file='individual (1).png')

photo2 = PhotoImage(file='family (1).png')

photo3 = PhotoImage(file='critical (1).png')

photo4 = PhotoImage(file='mediclaim (2).png')

photo5 = PhotoImage(file='senior (1).png')

photo6 = PhotoImage(file='accident (4).png')

photo7 = PhotoImage(file = "Back.png")
b7 = Button(root,text="", font=0, padx=50, pady=10,command=click7, image=photo7).place(x=90, y=670)

b1=Button(root,text="",font=('Times New Roman',20,'bold'),padx=120,pady=100, image=photo1, borderwidth=0, command=click1).place(x=70,y=60)

b2=Button(root,text="",font=('Times New Roman',20,'bold'),padx=25,pady=7, image=photo2, borderwidth=0, command=click2).place(x=70,y=390)

b3=Button(root,text="",font=('Times New Roman',20,'bold'),padx=25,pady=7, image=photo3, borderwidth=0, command=click3).place(x=380,y=60)

b4=Button(root,text="",font=('Times New Roman',20,'bold'),padx=25,pady=7, image=photo4, borderwidth=0, command=click4).place(x=380,y=390)

b5=Button(root,text="",font=('Times New Roman',20,'bold'),padx=25,pady=7, image=photo5, borderwidth=0, command=click5).place(x=680,y=60)

b6=Button(root,text="",font=('Times New Roman',20,'bold'),padx=25,pady=7, image=photo6, borderwidth=0, command=click6).place(x=680,y=390)

root.mainloop()

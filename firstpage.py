from tkinter import *

root = Tk()

root.geometry("1024x683")
root.title("Health Insurance Management System")

def click1():
    root.destroy()
    import Login

def click2():
    root.destroy()
    import Infoselect

def click3():
    root.destroy()
    import About

def click4():
    root.destroy()
    import FAQ




photo = PhotoImage(file='main.png')
labelph2 = Label(root, image = photo)

labelph2.place(x=0, y=0)

cancel1 = Button(root,bg='CadetBlue2', text="Sign in",font=('Times New Roman',18,'bold'), padx=40, pady=10,borderwidth=0,command=click1).place(x=40, y=20)
cancel2 = Button(root,bg='CadetBlue2', text="All Insurance",font=('Times New Roman',18,'bold'), padx=40, pady=10,borderwidth=0,command=click2).place(x=240, y=20)
cancel3 = Button(root, bg='CadetBlue2', text="About us",font=('Times New Roman',18,'bold'), padx=40, pady=10,borderwidth=0,command=click3).place(x=510, y=20)
cancel4 = Button(root,bg='CadetBlue2', text="FAQ",font=('Times New Roman',18,'bold'), padx=40, pady=10,borderwidth=0,command=click4).place(x=730, y=20)

root.mainloop()
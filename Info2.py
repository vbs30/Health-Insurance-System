from tkinter import *
import tkinter as tk


def click():
    root.destroy()
    import Infoselect


root = Tk()
root.title("Health Insurance Management System")
root.geometry("1000x800")
root.config(bg='white')

photo1 = PhotoImage(file = "Back.png")
b2 = Button(root,text="", font=0, padx=50, pady=10,command=click, image=photo1).place(x=80, y=670)
ini = Label(root, text="Critical Illness", bg='white',fg='dark magenta',font=("Times New Roman", 19, 'bold')).place(x=370, y=10)

U = Text(root, height=28, font=('Times New Roman', 14),width=95, borderwidth=0)
Fact1 = """A critical illness insurance cover, often referred in laymen language as Critical Illness Insurance, encompasses insurance benefits you receive to deal with life-threatening critical illnesses and various lifestyle diseases. Critical health issues like Cancer, Stroke, and Kidney failure require comprehensive treatment, which can take a toll on your finances are often covered in the Critical Illness Insurance Cover in addition to the base plan which provides a life insurance cover.

Benefits:

It acts as an income replacement: Critical ailments not only affect the person physically; it also has a major impact on the finances of the family. A critical insurance pays a lump sum amount which can be used to cover medical and household expenses.

It gives tax benefits: Critical illness payout is tax-free under Section 80D of the Income Tax Act.

It gives peace of mind: The policy gives peace of mind as now one can concentrate more on medical treatment rather than running around to arrange funds for medical and household expenses.

It covers treatment taking place in a foreign country: Under a critical illness insurance plan, a fixed sum is paid on the diagnosis of a critical ailment, irrespective of whether the treatment takes place in India or abroad. It means the policy can help you if you want to go abroad for further medical treatment.
 """

U.insert(tk.END, Fact1)
U.place(x=50, y=50)

root.mainloop()

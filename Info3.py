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
ini = Label(root, text="Mediclaim", bg='white',fg='dark magenta',font=("Times New Roman", 19, 'bold')).place(x=370, y=10)

U = Text(root, height=28, font=('Times New Roman', 14),width=95, borderwidth=0)
Fact1 = """Mediclaim is a viable option to safeguard yourself against the soaring healthcare expenses, arising because of hospitalization due to an illness or accident, without needing to incur any expenses from your own pocket.

This simply means that health insurance companies have collaborated with a number of hospitals across the country, known as "network hospitals," to provide cashless services to their policyholders. All the medical bills will directly get settled by the insurance company with the hospital upon availing of treatment at one of the network hospitals.
 
 Features and Benefits of Mediclaim Policy:
So, how does a mediclaim policy benefit you? Let’s look at some of the features and benefits of the policy:

It offers the ease of cashless hospitalisation.

You can opt for self or for the entire family.

It shields you from the financial burden.

Removes expenses paid from your pocket.

Insurance companies will handle the expenses arising out of hospitalisation.

Ease of buying through online health insurance companies.

It offers tax exemptions.

Avail cost-effective healthcare services.
 """

U.insert(tk.END, Fact1)
U.place(x=50, y=50)

root.mainloop()
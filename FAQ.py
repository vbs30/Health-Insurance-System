from tkinter import *

import tkinter as tk

def click7():
    root.destroy()
    import firstpage


root = Tk()
root.title("Health Insurance Management System")
root.geometry("1000x800")
root.config(bg='white')
l1 = Label(root,text="Q 1. What is health insurance?",font=('Times New Roman',18,'bold'),bg='white',fg='maroon').place(x=20,y=30)
#l2 = Label(root,text="Health insurance is an insurance product that provides cover for medical and surgical expenses of an insured person, in case of a medical emergency. However, you are required to pay a premium to avail health insurance policy.",font=('Times New Roman',18),bg='grey85',fg='grey2').place(x=20,y=60)
T1 = Text(root,font=('Times New Roman',16), height = 3, width = 88,borderwidth=0)
Fact1 = """\tHealth insurance is an insurance product that provides cover for medical and surgical expenses of an insured person, in case of a medical emergency. However, you are required to pay a premium to avail health insurance policy."""
T1.insert(tk.END, Fact1)
T1.place(x=10, y=80)
photo7 = PhotoImage(file = "Back.png")
b7 = Button(root,text="", font=0, padx=50, pady=10,command=click7, image=photo7).place(x=880, y=20)

l2 = Label(root,text="Q 2. Why should I buy health insurance?",font=('Times New Roman',18,'bold'),bg='white',fg='navy blue').place(x=20,y=200)
#l2 = Label(root,text="Health insurance is an insurance product that provides cover for medical and surgical expenses of an insured person, in case of a medical emergency. However, you are required to pay a premium to avail health insurance policy.",font=('Times New Roman',18),bg='grey85',fg='grey2').place(x=20,y=60)
T2 = Text(root,font=('Times New Roman',16), height = 3, width = 88,borderwidth=0)
Fact2 = """\tYou should purchase health insurance so that you don’t lose your lifelong savings while paying for medical bills in a critical situation."""
T2.insert(tk.END, Fact2)
T2.place(x=10, y=240)

l3 = Label(root,text="Q 3. What is the eligible age to buy health insurance?",font=('Times New Roman',18,'bold'),bg='white',fg='crimson').place(x=20,y=340)
#l2 = Label(root,text="Health insurance is an insurance product that provides cover for medical and surgical expenses of an insured person, in case of a medical emergency. However, you are required to pay a premium to avail health insurance policy.",font=('Times New Roman',18),bg='grey85',fg='grey2').place(x=20,y=60)
T3 = Text(root,font=('Times New Roman',16), height = 3, width = 88,borderwidth=0)
Fact3 = """\tWhile the eligibility age for health insurance policies differs, the general eligibility age for adults ranges between 18 years up to 65 years. The eligibility age for children lies between 90 days up to 18 years."""
T3.insert(tk.END, Fact3)
T3.place(x=10, y=390)

l4 = Label(root,text="Q 4. Will I be allowed to buy more than one health insurance plan?",font=('Times New Roman',18,'bold'),bg='white',fg='saddle brown').place(x=20,y=490)
#l2 = Label(root,text="Health insurance is an insurance product that provides cover for medical and surgical expenses of an insured person, in case of a medical emergency. However, you are required to pay a premium to avail health insurance policy.",font=('Times New Roman',18),bg='grey85',fg='grey2').place(x=20,y=60)
T4 = Text(root,font=('Times New Roman',16), height = 2, width = 88,borderwidth=0)
Fact4 = """\tYes, you are free to buy another plan based on your specific medical needs."""
T4.insert(tk.END, Fact4)
T4.place(x=10, y=530)

l5 = Label(root,text="Q 5. Can I pay my health insurance premium in installments?",font=('Times New Roman',18,'bold'),bg='white',fg='blue').place(x=20,y=600)
#l2 = Label(root,text="Health insurance is an insurance product that provides cover for medical and surgical expenses of an insured person, in case of a medical emergency. However, you are required to pay a premium to avail health insurance policy.",font=('Times New Roman',18),bg='grey85',fg='grey2').place(x=20,y=60)
T5 = Text(root,font=('Times New Roman',16), height = 2, width = 88,borderwidth=0)
Fact5 = """\tIn general, the health insurance premium is paid on a yearly basis. But, you can pay your premium in installments (monthly, quarterly or half-yearly basis) as well."""
T5.insert(tk.END, Fact5)
T5.place(x=10, y=640)

root.mainloop()
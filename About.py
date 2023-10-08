from tkinter import *
from tkinter import *

import tkinter as tk

def click7():
    root.destroy()
    import firstpage


root = Tk()
root.title("Health Insurance Management System")
root.geometry("1000x800")
root.config(bg='white')
l1 = Label(root,text="Our Vision ",font=('Times New Roman',24,'bold'),bg='white',fg='red').place(x=50,y=30)
T1 = Text(root,font=('Times New Roman',18), height = 3, width = 78,borderwidth=0)
Fact1 = """\tA State where each family is under the Universal Health Insurance Coverage receiving quality and affordable healthcare."""
T1.insert(tk.END, Fact1)
T1.place(x=10, y=90)
photo7 = PhotoImage(file = "Back.png")
b7 = Button(root,text="", font=0, padx=50, pady=10,command=click7, image=photo7).place(x=880, y=20)

l2 = Label(root,text="Our Mission",font=('Times New Roman',24,'bold'),bg='white',fg='navy blue').place(x=50,y=180)
#l2 = Label(root,text="Health insurance is an insurance product that provides cover for medical and surgical expenses of an insured person, in case of a medical emergency. However, you are required to pay a premium to avail health insurance policy.",font=('Times New Roman',18),bg='grey85',fg='grey2').place(x=20,y=60)
T2 = Text(root,font=('Times New Roman',18), height = 3, width = 76,borderwidth=0)
Fact2 = """\tReducing the out of pocket expenditure of families enrolled under the scheme and in the process, improving the health care services of the State."""
T2.insert(tk.END, Fact2)
T2.place(x=10, y=230)

l3 = Label(root,text="Our Objectives",font=('Times New Roman',24,'bold'),bg='white',fg='brown').place(x=50,y=340)
T3 = Text(root,font=('Times New Roman',18), height =12, width = 77,borderwidth=0)
Fact3 = """1)To create a sustainable and practical universal health insurance scheme for the residents of     \tthe State of Meghalaya.
2)To enhance the hospital network, implementation, administration, enrolment and utilization of the benefits under the Scheme.
3)To adhere to quality database maintenance of the population of the State.
4)Ensuring costing packages are monitored rigorously which is aimed at minimizing out-of-pocket expenditure.
5)To provide adequate cover after considering the incidence rate of regional diseases and diseases or illnesses requiring tertiary care procedures.
6)To improve the overall service quality, including patient care facilities
7)To provide strong quality control, monitoring and fraud control mechanisms.
8)To strengthen citizen voice and empower patients by influencing their health seeking behaviors."""
T3.insert(tk.END, Fact3)
T3.place(x=30, y=400)

root.mainloop()

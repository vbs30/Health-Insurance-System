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

ini = Label(root, text="Family Health Insurance", bg='white',fg='dark magenta',font=("Times New Roman", 19, 'bold')).place(x=370, y=10)

U = Text(root, height=28, font=('Times New Roman', 14),width=95, borderwidth=0)
Fact1 = """ A family floater is a health insurance plan that extends the coverage to the entire family rather than just an individual as in the case of an individual plan. In simple words, health insurance plans for family bring all the members of the family under a common umbrella of the sum insured. By getting covered under a floater plan, every member of the family gets benefits under a larger common pool.

Benefits of Family Floater Health Insurance Plans

Following are the key benefits of a family floater health insurance plan

1. Coverage for the entire family

Floater Pans allow you to enjoy cover for the entire family under one plan, it may include you, your spouse, dependent children, and dependent parents.

2. The premiums are affordable

The premium payable for the entire family is cheaper than that of individual plans, as in case you are planning to buy separate insurance plans for all the family members, you would require to pay a premium on all the plans separately, while in the case of floater plans the entire family would be covered under same premium amount, which makes it easily affordable.

3. Every member gets high coverage

Every member can use the whole amount of sum insured in the policy if they fall ill, each family member has complete access to the sum insured.

If you have a small budget and plans to buy an individual plan for the entire family you would buy plans with the less-sum insured amount, but in the case of floater plans, you can buy a high coverage plan for the whole family in the same budget.
"""

U.insert(tk.END, Fact1)
U.place(x=50, y=50)

root.mainloop()
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

T = Text(root, height=28, width=95, font=('Times New Roman', 14), borderwidth=0)
ini = Label(root, text="Individual Insurance", bg='white',fg='dark magenta',font=("Times New Roman", 19, 'bold')).place(x=370, y=10)

Fact = """Individual health insurance is a policy that provides financial aid in case the policyholder requires medical assistance. An individual health insurance plan covers the medical expenses of an insured individual and offers benefits like cashless hospitalization, easy medication, and prompt services, among other things.

The premium for an individual health insurance plan is decided as per the sum insured opted for, medical history and age of the person buying the policy. You should start planning after the age of 18 since any kind of health policy could turn out to be beneficial.

Benefits of Individual Health Insurance
There are various benefits of buying individual health insurance:

Customized Benefits:

Individual health insurance is tailor-made, and you can choose the one that best fits your needs. You can have coverage for a specific disorder, e.g., critical illness and personal accident cover. Some individual health insurance plans provide maternity coverage wherein ladies can get coverage regarding pregnancy expenses.

Assured Coverage Amount: If you purchase individual health insurance, you have a definite amount that is used towards your healthcare requirements. As such, you will no longer have to worry about dipping into your savings in case you contract any disease.

Coverage built for you:

The sum insured offered under the individual health insurance plan is available solely for you. As opposed to the family floater plan, where the sum insured is utilized by all the insured members as and when the need arises.

Risks and Premium:

Not every policy might suit you. You need to be practical when selecting an individual health insurance plan and ensure that it's the best one for your needs and requirements. If you opt for a family floater, it might end up being a costlier option since age acts as a risk factor in increasing the premium. In such a case, you should preferably go for individual health insurance.
 """
T.insert(tk.END, Fact)
T.place(x=50, y=50)

root.mainloop()

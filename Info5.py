from tkinter import *
import tkinter as tk


def click():
    root.destroy()
    import Infoselect


root = Tk()
root.title("Health Insurance Management System")
root.geometry("1000x800")
root.config(bg='white')
my_image = PhotoImage(file='loginnew.png')


photo1 = PhotoImage(file = "Back.png")
b2 = Button(root,text="", font=0, padx=50, pady=10,command=click, image=photo1).place(x=80, y=670)
ini = Label(root, text="Accidental Cover", bg='white',fg='dark magenta',font=("Times New Roman", 19, 'bold')).place(x=370, y=10)

U = Text(root, height=28, font=('Times New Roman', 14),width=95, borderwidth=0)
Fact1 = """An accident can occur at any time without any warning, and sometimes it can cause serious harm. Any such untoward incident can have a significant impact on your finances; not only can the treatment be expensive, but if you suffer from any form of disability, it can affect your earning potential. To protect yourself and your family from such a situation, it is paramount that you purchase a personal accident insurance policy.

Personal accident insurance is useful to get the financial assistance to you and your family in the event of an accident that leads to death, bodily injuries, temporary total disability, permanent total disability and permanent partial disability. In the event of death, the insurance company will pay 100% compensation (equal to the sum assured) to the appointed nominee.

Personal Accident insurance has many benefits, which are:

Peace of mind and family security
In the event of an accident that causes death or renders you disabled, it would have a significant impact on your earning potential. An accident cover will give your family financial protection in the form of accidental compensation and ensure their financial security. The insurance companies pay 100% compensation in the event of death. The family members can use the amount to pay off the liabilities (if any) and maintain the usual lifestyle. Also, it gives you the peace of mind knowing that your family will be financially secured even in your absence.

Minimal documentation
One of the significant reasons why a lot of people avoid buying insurance is that they believe the process is complicated, and it involves a lot of paper works. However, the truth is that when you purchase a personal accident insurance policy, you need not stress about the documentation. You must provide basic details in the application form, and the insurance company will issue the policy.

No medical tests required
This is another significant benefit of an accident insurance policy. Unlike the health insurance policy, where the insurance company requires you to undergo medical tests before issuing the policy, you need not take any tests.

 """

U.insert(tk.END, Fact1)
U.place(x=50, y=50)

root.mainloop()
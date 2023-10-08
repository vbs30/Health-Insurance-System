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
ini = Label(root, text="Senior Citizen", bg='white',fg='dark magenta',font=("Times New Roman", 19, 'bold')).place(x=370, y=10)

U = Text(root, height=28, font=('Times New Roman', 14),width=95, borderwidth=0)
Fact1 = """Old age brings with itself several ailments that are expensive to treat and care for. Health insurance for Senior Citizens is offered by various insurance companies, specifically for people who are aged 65 years and above. These health insurance schemes readily cover any kind of medical expenses incurred by customers.

The older we get, the more our physical and mental stress over finances and the ability to afford good healthcare. A senior citizen health insurance plan is designed to offer financial aid for medical treatments to individuals over 60 years of age in their hour of need. Senior citizen health insurance plans offer critical illness cover, cashless hospitalisation, pre-existing disease cover, and a higher sum assured.

Following are the benefits of availing a senior citizen health insurance scheme for your parents –

Tax benefit on medical insurance premium
Avail treatment and medical facilities across a host of hospitals across the nation
Enjoy Cashless treatment and daily allowance (depends on insurer)
Renewal of policy option
Domiciliary Hospitalization cover
Enjoy free-look period
Avail health check-ups annually
Reload of sum insured

 """

U.insert(tk.END, Fact1)
U.place(x=50, y=50)

root.mainloop()
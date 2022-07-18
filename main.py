import tkinter
from webbrowser import get
from forex_python.converter import CurrencyRates
from tkinter import *
from tkinter.ttk import Combobox
# tk innter to Display
window=tkinter.Tk()
window.title('currency converter')
window.geometry('1000x1000')
#heading
heading=tkinter.Label(window,text="Welcome to Currency converter ",fg='blue',bg='yellow',font=("arial,Bold",20))
heading.grid(column=15,row=0)
#text for entry
amount=tkinter.Label(window,text="Enter the Amount",fg='blue',font=("arial,Bold",10))
From_Currency=tkinter.Label(window,text="From Currency: ",fg='blue',font=("arial,Bold",10))
to_currency=tkinter.Label(window,text="to currency",fg='blue',font=("arial,Bold",10))
amount.grid(column=7,row=3)
From_Currency.grid(column=7,row=5)
to_currency.grid(column=7,row=8)
# to communiate with user
input1=tkinter.Entry(window,width=30,fg='blue')
input2=tkinter.Entry(window,width=30,fg='blue')
input3=tkinter.Entry(window,width=30,fg='blue')
input1.grid(column=8,row=3)
input2.grid(column=8,row=5)
input3.grid(column=8,row=8)
# result output
l2=tkinter.Label(window,text="",fg='blue',font=("arial,Bold",10))
l2.grid(column=2,row=15)
# EXAMPLES:
EXAMPLES1=tkinter.Label(window,text=" EXAMPLS OF CODE \n country \t code ",fg='blue' ,font=("arial,Bold",15))
EXAMPLE2=tkinter.Label(window,text="INDIA \t INR \nUSA \t USD \nAustralia \t AUD \nJapan \t JPY \n \tZimbabwe \t ZWD ",fg='orange',font=("arial,Bold",10))
EXAMPLES1.grid(column=2,row=19)
EXAMPLE2.grid(column=2,row=20)
#result process
def converstion():
    c = CurrencyRates()
    result1 = c.convert(input3.get().upper(), input2.get().upper(), int(input1.get().upper()))
    l2.configure(text=result1)

bt=tkinter.Button(window,text='enter',fg='blue',bg='yellow', width=20,command=converstion)
bt.grid(column=8,row=17)
window.mainloop()

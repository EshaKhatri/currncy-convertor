from tkinter import Tk, ttk
from tkinter import *

import requests
import json

from PIL import Image, ImageTk

window = Tk()

cor0="#FFFFFF"
cor1="#333333"
cor2="#EB5D51"

window.geometry('300x320')
window.title('Currency Converter')
window.configure(bg=cor0)
window.resizable(width=False, height=False)

top = Frame(window,width=300,height=60,bg=cor2)
top.grid(row=0,column=0)

main = Frame(window,width=300,height=260,bg=cor0)
main.grid(row=1,column=0)

def convert():
    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

    currency_1 = combo1.get()
    currency_2 = combo2.get()
    amount=value.get()

    querystring = {"from":currency_1,"to":currency_2,"amount":amount}

    headers = {
	    "X-RapidAPI-Key": "33ec956489mshe3576a6601ce4b4p189d5fjsn86e032ac4476",
	    "X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    data=json.loads(response.text)
    converted_Amount = data['result']['convertedAmount']
    formatted = currency_2 + " {:,.2f}".format(converted_Amount)

    result['text']=formatted

    print(converted_Amount,formatted)



#top frame

icon = Image.open('images/icons.png')
icon = icon.resize((40,40))
icon = ImageTk.PhotoImage(icon)
app_name = Label(top, image=icon, compound=LEFT, text="Currency Converter", height=5, padx=13, pady=25, anchor=CENTER, font=('Arial 16 bold'), bg=cor2, fg=cor1)
app_name.place(x=0,y=0)

#main frame

result = Label(main, text="", height=2, width = 19, pady=7, anchor=CENTER, font=('Arial 15'), bg=cor0, fg=cor1, relief="solid")
result.place(x=50,y=10)

currency = ['CAD' , 'BRL', 'EUR', 'INR','USD']


fromm = Label(main, text="From", height=1, width = 8, pady=0,padx=0, anchor=NW, font=('Arial 10 bold'), bg=cor0, fg=cor1, relief="flat")
fromm.place(x=48,y=90)

combo1 = ttk.Combobox(main, width=8, justify=CENTER, font=("arial 12 bold"))
combo1['values']=(currency)
combo1.place(x=50,y=115)

to = Label(main, text="To", height=1, width = 8, pady=0,padx=0, anchor=NW, font=('Arial 10 bold'), bg=cor0, fg=cor1, relief="flat")
to.place(x=158,y=90)

combo2 = ttk.Combobox(main, width=8, justify=CENTER, font=("arial 12 bold"))
combo2['values']=(currency)
combo2.place(x=160,y=115)

value = Entry(main, width=22, justify=CENTER,font=('arial 12 bold'), relief="solid")
value.place(x=50,y=155)

button  = Button(main, text="Converter", width=19, padx=5,height=1,bg=cor2,fg=cor1,font=('arial 12 bold'), command=convert)
button.place(x=50,y=190)


window.mainloop()
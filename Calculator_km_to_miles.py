from tkinter import *

window=Tk()

window.title("Miles to Km Convertor")

window.config(padx=40,pady=40)

window.minsize(width=500,height=200)

label1=Label(text="Miles")

label1.grid(column=3,row=2)

label2=Label(text="km")

label2.grid(column=3,row=3)

label3=Label(text="is equal to")

label3.grid(column=0,row=2)

miles=Entry()

miles.grid(column=1,row=2)

km=Entry()

km.grid(column=1,row=3)

def cal():

    miles_user=float(miles.get())

    calcute= miles_user*1.60934

    km.delete(0,END)

    km.insert(END,string=calcute)

button=Button(text="Calculate",command=cal)

button.grid(column=1,row=4)





window.mainloop()
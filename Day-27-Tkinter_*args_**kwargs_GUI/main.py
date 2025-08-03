from tkinter import *


window=Tk()
window.title("Miles to Kilometer Convertor")
window.minsize(300,200)
window.config(padx=40,pady=40)

#Entry
enterr = Entry(width=10)
enterr.get()
enterr.insert(END, string="0")
enterr.grid(column=1, row=0)

#label
my_label = Label(text="Miles",font=("Arial",20,"bold"))
my_label.grid(column=2,row=0)

label2 = Label(text="is equal to",font=("Arial",20,"bold"))
label2.grid(column=0,row=1)

label3 = Label(text="Km",font=("Arial",20,"bold"))
label3.grid(column=2,row=1)

label4 = Label(text="0",font=("Arial",20,"bold"))
label4.grid(column=1,row=1)

#button
def button_clicked():
    new_text= enterr.get()
    ans= float(new_text) * 1.609
    label4.config(text=f"{round(ans,2)}")
    return ans

button  = Button(text="Calculate",command=button_clicked)
button.grid(column=1,row=2)

window.mainloop()

from tkinter import *
import pandas as pd
from random import choice

secs=5
timer_status= ""
BACKGROUND_COLOR = "#B1DDC6"

# ------------------------------- DATA --------------------------------- #
try:
    words_bank = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    words_bank = pd.read_csv("./data/data.csv")

zagost = {row.Turkish: row.English for (index, row) in words_bank.iterrows()}

random_key = choice(list(zagost.keys()))
random_value = zagost[random_key]

# ------------------------------ TIMER --------------------------------- #
def timerr(secs,random_key,random_value):
    global timer_status
    if secs>0:
        timer_status = window.after(1000, timerr, secs - 1, random_key, random_value)
    else:
        canvas.itemconfig(cardd_hold,image=card_back)
        canvas.itemconfig(card_title,text="English",fill="white")
        canvas.itemconfig(card_word,text=f"{random_value}",fill="white")

def reset_this():
    global timer_status
    if timer_status:
        window.after_cancel(timer_status)

# ---------------------------- NEW WORD ------------------------------- #
def delete_known():
    global random_key  # Access the current `random_key`
    try:
        del zagost[random_key]
        shit = pd.DataFrame(list(zagost.items()),columns=["Turkish","English"])
        shit.to_csv("./data/words_to_learn.csv",index=False)
    except KeyError:
        pass
    new_word()

def new_word():
    global random_key,random_value
    reset_this()
    random_key = choice(list(zagost.keys()))
    random_value = zagost[random_key]

    print(random_value,random_key)
    canvas.itemconfig(card_title,text = "Turkish",fill=BACKGROUND_COLOR)
    canvas.itemconfig(card_word,text = f"{random_key}",fill=BACKGROUND_COLOR)
    canvas.itemconfig(cardd_hold,image=card_front)

    timerr(secs,random_key,random_value)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flash Me!")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

canvas= Canvas(width=800,height=526,highlightthickness=0)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
cardd_hold = canvas.create_image(400,263, image=card_front)
canvas.grid(row=0,column=0,columnspan=2)
card_title = canvas.create_text(400,150,text="",font=("Ariel",40,"italic"))
card_word = canvas.create_text(400,263,font=("Ariel",60,"bold"),text=f"")

#Buttons
noo_img= PhotoImage(file="./images/wrong.png")
no_button = Button(image=noo_img,highlightthickness=0,command=new_word)
no_button.grid(row=1,column=0)
yee_img = PhotoImage(file="./images/right.png")
yes_button = Button(image=yee_img,highlightthickness=0,command=delete_known)
yes_button.grid(row=1,column=1)


new_word()

window.mainloop()


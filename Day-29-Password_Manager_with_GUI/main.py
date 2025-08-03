from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for x in range(randint(8, 10))]
    password_list += [choice(numbers)  for x in range(randint(2, 4))]
    password_list += [choice(symbols) for x in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    entry_password.insert(0, f"{password}")
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    liss=[entry_website.get(),entry_username.get(),entry_password.get()]
    end = " | ".join(liss)
    if len(entry_password.get())==0 or len(entry_website.get()) ==0 or len(entry_username.get()) ==0:
        messagebox.showinfo(title="Oopsie Daisy", message="Please don't leave any fields empty bro chan")
    else:
        is_ok = messagebox.askokcancel(title=entry_website.get(),
                                       message=f"These are the details entered: \n Email:{entry_username.get()}"
                                               f"Password:{entry_password.get()}\n Is it ok to save?")
        if is_ok:
            with open("data.txt","a") as file:
                file.write(f"{str(end)}\ne")
            entry_password.delete(0,END)
            entry_website.delete(0,END)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Abdo's Password Manager")
window.config(padx=50,pady=50)

canvas= Canvas(width=200,height=200,highlightthickness=0)
logoo = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logoo)
canvas.grid(column=2,row=1)

    #labels
label_website = Label(text="Website:")
label_website.grid(column=1,row=2)

label_email = Label(text="Email/Username:")
label_email.grid(column=1,row=3)

label_password = Label(text="Password:")
label_password.grid(column=1,row=4)


    #Entries
entry_website = Entry(width=35)
entry_website.grid(column=2,row=2,columnspan=2)
entry_website.focus()

entry_username = Entry(width=35)
entry_username.grid(column=2,row=3,columnspan=2)
entry_username.insert(0,"your_email@gmail.com")

entry_password = Entry(width=18)
entry_password.grid(column=2,row=4)
        #Gets text in entry
entry_website.get()
entry_username.get()
entry_password.get()


    #buttons
#calls action() when pressed
generate = Button(text="Generate Password",command=generate_password)
generate.grid(column=3,row=4)

add = Button(text="Add",width=33,command=save)
add.grid(column=2,row=5,columnspan=2)


window.mainloop()

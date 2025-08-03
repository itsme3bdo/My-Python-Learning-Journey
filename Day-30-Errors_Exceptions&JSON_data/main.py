from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip
import json

# ------------------------------- FIND PASSWORD --------------------------------- #
def find_pass():
    website = entry_website.get()
    try:
        with open("data.json") as file:
            # we read the  old data
            info = json.load(file)
    except  FileNotFoundError:
        messagebox.showinfo(title=f"Error", message=f"No Data File Found")
    else:
        for x in info.keys():
            if x == website.title():
                email = info[x]["email"]
                passo = info[x]["password"]
                messagebox.showinfo(title=f"{x}", message=f"Username:{email}\nPassword:{passo}")
            else:
                messagebox.showinfo(title="Error", message=f"No details for {website} exists")

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
    website = entry_website.get()
    email  = entry_username.get()
    password = entry_password.get()
    new_data = {
        website.title(): {
            "email":email,
            "password":password
        }
    }
    if len(website)==0 or len(email) ==0 or len(password) ==0:
        messagebox.showinfo(title="Oopsie Daisy", message="Please don't leave any fields empty bro chan")
    else:
        is_ok = messagebox.askokcancel(title=entry_website.get(),
                                       message=f"These are the details entered: \n Email:{email}"
                                               f"Password:{password}\n Is it ok to save?")
        if is_ok:
            try:
                with open("data.json","r") as file:
                    # we read the  old data
                    info = json.load(file)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data,file,indent=4)
            else:
                # we update the old data with new data
                info.update(new_data)
                with open("data.json", "w") as file:
                    #save updated data
                    json.dump(info,file,indent=4)
            finally:
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
entry_website = Entry(width=18)
entry_website.grid(column=2,row=2)
entry_website.focus()

entry_username = Entry(width=35)
entry_username.grid(column=2,row=3,columnspan=2)
entry_username.insert(0,"bodeman2000@gmail.com")

entry_password = Entry(width=18)
entry_password.grid(column=2,row=4)
        #Gets text in entry
entry_website.get()
entry_username.get()
entry_password.get()


    #buttons
#calls action() when pressed
search = Button(text="Search",command=find_pass,width=12)
search.grid(column=3,row=2)

generate = Button(text="Generate Password",command=generate_password,width=13)
generate.grid(column=3,row=4)

add = Button(text="Add",width=33,command=save)
add.grid(column=2,row=5,columnspan=2)

window.mainloop()

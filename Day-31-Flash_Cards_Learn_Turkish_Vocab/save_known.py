from tkinter import *
import pandas as pd
from random import choice
import os # Import the os module
import sys # Import the sys module

secs = 5
timer_status = ""
BACKGROUND_COLOR = "#B1DDC6"

# --- Helper function for PyInstaller paths ---
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
# ---------------------------------------------


# ------------------------------- DATA --------------------------------- #
# This will hold all words from data.csv that haven't been learned yet, in order
words_to_learn_list = []
# This will hold words marked as learned across sessions
learned_words_list = []

# 1. Load all words from your pristine data.csv
try:
    # Use resource_path for data.csv
    data_df = pd.read_csv(resource_path("data/data.csv"))
    all_words_from_data = data_df.to_dict(orient="records")
except FileNotFoundError:
    print("Error: data.csv not found! Please ensure 'data' folder and 'data.csv' exist.")
    sys.exit(1) # Use sys.exit() instead of exit()

# 2. Load previously learned words (if any)
try:
    # Use resource_path for learned_words.csv
    learned_df = pd.read_csv(resource_path("data/learned_words.csv"))
    learned_words_list = learned_df.to_dict(orient="records")
except FileNotFoundError:
    # If learned_words.csv doesn't exist yet, it's okay, it will be created.
    learned_words_list = []

# 3. Filter out already learned words from the main data to create the current session's words_to_learn_list
# Create a set of learned Turkish words for efficient lookup
learned_turkish_words_set = {word['Turkish'] for word in learned_words_list}

# Populate words_to_learn_list with words from data.csv that are NOT in the learned set
for word_data in all_words_from_data:
    if word_data['Turkish'] not in learned_turkish_words_set:
        words_to_learn_list.append(word_data)

# This will hold the current word being displayed
current_word_data = {}

# ------------------------------ TIMER --------------------------------- #
def timerr(secs, word_data):
    global timer_status
    if secs > 0:
        timer_status = window.after(1000, timerr, secs - 1, word_data)
    else:
        canvas.itemconfig(cardd_hold, image=card_back)
        canvas.itemconfig(card_title, text="English", fill="white")
        canvas.itemconfig(card_word, text=f"{word_data['English']}", fill="white")

def reset_this():
    global timer_status
    if timer_status:
        window.after_cancel(timer_status)

# ---------------------------- WORD LOGIC ------------------------------- #

def delete_known():
    """Moves the current word from words_to_learn_list to learned_words_list."""
    global words_to_learn_list, learned_words_list, current_word_data

    if current_word_data: # Ensure there's a word currently displayed
        learned_words_list.append(current_word_data)
    new_word()

def new_word():
    """Displays the next word from words_to_learn_list (the top one)."""
    global current_word_data, words_to_learn_list
    reset_this() # Reset the timer for the previous word

    if not words_to_learn_list:
        canvas.itemconfig(card_title, text="No more words!", fill=BACKGROUND_COLOR)
        canvas.itemconfig(card_word, text="Great job! All words learned.", fill=BACKGROUND_COLOR)
        # Disable buttons if all words are learned
        no_button.config(state="disabled")
        yes_button.config(state="disabled")
        save_data() # Save all progress
        return

    # Get the first word from the list and remove it (to display it)
    current_word_data = words_to_learn_list.pop(0)

    print(f"Current word: {current_word_data['Turkish']} - {current_word_data['English']}")
    canvas.itemconfig(card_title, text="Turkish", fill=BACKGROUND_COLOR)
    canvas.itemconfig(card_word, text=f"{current_word_data['Turkish']}", fill=BACKGROUND_COLOR)
    canvas.itemconfig(cardd_hold, image=card_front)

    timerr(secs, current_word_data)

def next_word_unknown():
    """Puts the current word back to the end of words_to_learn_list and gets a new one."""
    global words_to_learn_list, current_word_data
    if current_word_data: # Ensure there's a word to re-add
        words_to_learn_list.append(current_word_data) # Add to the end for later review
    new_word()

def save_data():
    """Saves the current state of learned words to learned_words.csv."""
    # We only save the learned words, as 'words to learn' are derived from data.csv each run
    learned_df = pd.DataFrame(learned_words_list)
    # Use resource_path for saving learned_words.csv
    learned_df.to_csv(resource_path("data/learned_words.csv"), index=False)
    print("Progress saved!")
    window.destroy() # Add this line to properly close the Tkinter window and exit mainloop


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flash Me!")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

canvas= Canvas(width=800,height=526,highlightthickness=0)
# Use resource_path for image files
card_front = PhotoImage(file=resource_path("images/card_front.png"))
card_back = PhotoImage(file=resource_path("images/card_back.png"))
cardd_hold = canvas.create_image(400,263, image=card_front)
canvas.grid(row=0,column=0,columnspan=2)
card_title = canvas.create_text(400,150,text="",font=("Ariel",40,"italic"))
card_word = canvas.create_text(400,263,font=("Ariel",60,"bold"),text=f"")

#Buttons
noo_img= PhotoImage(file=resource_path("./images/wrong.png")) # Using resource_path
no_button = Button(image=noo_img,highlightthickness=0,command=next_word_unknown)
no_button.grid(row=1,column=0)

yee_img = PhotoImage(file=resource_path("./images/right.png")) # Using resource_path
yes_button = Button(image=yee_img,highlightthickness=0,command=delete_known)
yes_button.grid(row=1,column=1)

# Ensure data is saved when the window is closed
window.protocol("WM_DELETE_WINDOW", save_data)

# Start the first word
new_word()

window.mainloop()


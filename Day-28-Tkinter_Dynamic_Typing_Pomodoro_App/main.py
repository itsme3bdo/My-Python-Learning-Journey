import math
from tkinter import *
from tkinter import messagebox
from playsound import playsound
from tkinter import ttk

current_session_time=0

# ----------------------------- POP UP --------------------------------- #
damn=-1
def pop_up(reps):
    global damn
    damn+=1
    if reps==1:
        pass
    elif damn % 8 == 0:
        window.focus_force()
        playsound("titanic.mov")
        messagebox.showinfo("Break Ended", "Your long break ended! Time to hustle my boi")
    elif damn %2==0:
        window.focus_force()
        playsound("Bruh.mp3")
        messagebox.showinfo("Break Ended", "Your short break ended! Hustle baby")
    else:
        window.focus_force()
        playsound("wind.m4a")
        messagebox.showinfo("Session Ended", "Your work session has ended! Time for a break!")


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 0.1
check="✓"
reps=0
timerr=None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_this():
    window.after_cancel(timerr)
    global reps
    reps=0
    canvas.itemconfig(timer_text,text="00:00")
    timer_label.config(text="Timer")
    check_label.config(text="")
    progress['value']=0
# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps,current_session_time
    reps+=1
    work_sec= WORK_MIN * 60
    short_break_sec= SHORT_BREAK_MIN * 60
    long_break_sec= LONG_BREAK_MIN * 60

    if reps%8==0:
        current_session_time = long_break_sec  # Set total time for the long break
        count_down(long_break_sec)
        pop_up(reps)
        timer_label.config(text="Break",fg=RED)
    elif reps%2==0:
        current_session_time = short_break_sec  # Set total time for the short break
        count_down(short_break_sec)
        pop_up(reps)
        timer_label.config(text="Break", fg=PINK)
    else:
        current_session_time = work_sec  # Set total time for the work session
        count_down(work_sec)
        pop_up(reps)
        timer_label.config(text="Work",fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global current_session_time  # Total time for the current session
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global timerr,time_elap
        timerr=window.after(1000,count_down,count-1)


        progress['value'] = ((current_session_time - count) / current_session_time) * 100
        window.update_idletasks()

    else:
        start_timer()
        mark=""
        work_sessions=math.floor(reps/2)
        for x in range(work_sessions):
            mark+="✓"
        check_label.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Abdo's Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)


canvas= Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=2,row=2)


    #progress bar

progress = ttk.Progressbar(window,length=200,mode='determinate')
progress.grid(column=2, row=3)

timer_label = Label(text="Timer",bg=YELLOW,fg=GREEN,font=(FONT_NAME,40,"normal"))
timer_label.grid(column=2,row=1)


start_button  = Button(text="Start",bg=YELLOW,highlightbackground=YELLOW,command=start_timer)
start_button.grid(column=1,row=3)

reset_button  = Button(text="Reset",bg=YELLOW,highlightbackground=YELLOW,command=reset_this)
reset_button.grid(column=3,row=3)

check_label=Label(bg=YELLOW,fg=GREEN,font=(FONT_NAME,30,"normal"))
check_label.grid(column=2,row=4)
window.mainloop()

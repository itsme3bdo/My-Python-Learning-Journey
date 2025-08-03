from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
class QuizInterface:

    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.score = Label(text=f"Score:{self.quiz.score}",fg="white",bg=THEME_COLOR)
        self.score.grid(row=0,column=1)

        self.canvas = Canvas(width=300,height=250,bg="white",highlightthickness=0)
        self.text = self.canvas.create_text(150,125,width=280, text="",fill=THEME_COLOR,font=("Arial",20,"italic"))

        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)


        noo_img = PhotoImage(file="images/false.png")
        self.no_button = Button(image=noo_img, highlightthickness=0,command=self.wrong)
        self.no_button.grid(row=2, column=1)

        yes_img = PhotoImage(file="images/true.png")
        self.yes_button = Button(image=yes_img, highlightthickness=0,command=self.right)
        self.yes_button.grid(row=2, column=0)

        self.next_question()

        self.window.mainloop()

    def right(self):
        self.score.config(text=f"Score:{self.quiz.score}/{self.quiz.question_number}")
        self.feedback(self.quiz.check_answer("True"))

    def wrong(self):
        self.score.config(text=f"Score:{self.quiz.score}/{self.quiz.question_number}")
        self.feedback(self.quiz.check_answer("False"))


    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text,text=q_text)
        else:
            self.canvas.itemconfig(self.text,text="You have reached the end of the quiz")
            self.no_button.config(state="disabled")
            self.yes_button.config(state="disabled")


    def feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.next_question)







from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l=0
        self.r=0
        self.update_score()

    def update_score(self):
        self.goto(-100,200)
        self.write(self.l,align="center",font=("Courier",80,"normal"))
        self.goto(100, 200)
        self.write(self.r, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.l+=1
        self.clear()
        self.update_score()

    def r_point(self):
        self.r+=1
        self.clear()
        self.update_score()


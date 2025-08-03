from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-290,270)
        self.level=0
        self.update_scoreboard()

    def gameover(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=('Arial', 20, "normal"))

    def update_scoreboard(self):
        self.level+=1
        self.clear()
        self.write(f"Level: {self.level}", align="left",font=FONT)



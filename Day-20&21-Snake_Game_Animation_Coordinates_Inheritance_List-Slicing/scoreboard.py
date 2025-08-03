from turtle import Turtle

file = open("data.txt")
contents =  file.read()
file.close()

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.highscore=int(contents)
        self.goto(0,270)
        self.color("green")
        self.update_scoreboard()
        self.hideturtle()

    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.highscore} ")

        self.score=0
        self.update_scoreboard()


    def add_1(self):
        self.score +=  1
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", False, "center", ('Arial', 20, "normal"))


    # def gameover(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER",align="center",font=('Arial',20,"normal"))



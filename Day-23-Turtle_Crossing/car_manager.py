from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.seeed = STARTING_MOVE_DISTANCE
        self.shape("square")
        self.shapesize(1,2)
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(320,random.randint(-250,250))

    def arrive(self):
        self.backward(self.seeed)

    def incres(self):
        self.seeed+=MOVE_INCREMENT

    def gen(self):
        return random.randint(0,100)%2==0




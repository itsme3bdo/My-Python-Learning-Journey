from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.direc=1
        self.xup=10
        self.yup=10
        self.penup()
        self.shape("circle")
        self.shapesize(1,1)
        self.color("white")
        self.move_speed=0.1

    def move(self):
        new_x=self.xcor()+(self.xup*self.direc)
        new_y=self.ycor()+(self.yup*self.direc)
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.yup*=-1

    def bounce_x(self):
        self.xup*=-1
        self.move_speed *= 0.9

    def reseet(self):
        self.goto(0,0)
        self.bounce_x()
        self.move_speed = 0.1


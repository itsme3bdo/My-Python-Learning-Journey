from turtle import Turtle

from skimage.filters.lpi_filter import forward
forwardd = 20
class Paddle(Turtle):
    def __init__(self,xcorr,ycorr):
        super().__init__()
        self.penup()
        self.shapesize(5,1)
        self.shape("square")
        self.setposition(xcorr,ycorr)
        self.color("white")

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)





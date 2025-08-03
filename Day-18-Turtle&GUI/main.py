import turtle
from pickle import GLOBAL
from random import randint
from turtle import Turtle, Screen
import random

color_list = [(179, 11, 33), (183, 172, 13), (187, 74, 23), (248, 214, 73), (212, 157, 76), (171, 23, 16), (114, 185, 204), (50, 96, 159), (61, 48, 109), (224, 128, 160)]

mody = Turtle()
mody.shape("turtle")
turtle.colormode(255)
mody.speed(10)
mody.hideturtle()

def rand_color():
    # r = randint(0,255)
    # g = randint(0,255)
    # b = randint(0,255)
    # khod =  (r,g,b)
    khod = random.choice(color_list)
    return khod



# for x in range(3,11):
#     z=0
#     mody.pencolor(random.choice(colorz))
#     while z<x:
#         mody.forward(100)
#         mody.right(360/x)
#         z += 1

def random_dic():
    left_right = random.randint(1,2)
    if  left_right == 1:
        ooo = random.randint(1, 4)
        mody.right(ooo * 90)
    else:
        ooo = random.randint(1, 4)
        mody.left(ooo * 90)

def turn_left():
    mody.left(90)
    mody.dot(20)
    mody.forward(50)
    mody.left(90)
    global lvl
    lvl += 1

def turn_right():
    mody.right(90)
    mody.dot(20)
    mody.forward(50)
    mody.right(90)
    global lvl
    lvl += 1

mody.penup()
lvl=0
z=0
while lvl != 10 and z!=10:
    mody.color(rand_color())
    mody.dot(20)
    mody.forward(50)
    z+=1
    if z == 9 and lvl%2==0:
        z=0
        turn_left()
    elif z==9 and lvl%2!=0:
        turn_right()
        z=0




# angle=0
# while angle !=360:
#     angle+=5
#     mody.color(rand_color())
#     mody.speed(0)
#
#     # mody.pensize(15)
#     # random_dic()
#     # mody.forward(30)
#     mody.circle(100)
#     mody.setheading(angle)
#     mody.setposition((0,0))

screen = Screen()
screen.exitonclick()

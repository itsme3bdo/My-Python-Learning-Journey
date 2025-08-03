from random import random, randint
from turtle  import Turtle,Screen

# bud = Turtle()
# screen=Screen()
# bud.speed(10)
# angle=0
# def move_forward():
#     bud.forward(25)
# def move_backwards():
#     bud.backward(25)
# def counter_clockwise():
#     global angle
#     angle+=10
#     bud.setheading(angle)
# def clockwise():
#     global angle
#     angle -= 10
#     bud.setheading(angle)
# def clear():
#     bud.clear()
#     bud.penup()
#     bud.home()
#     bud.pendown()
#
#
#
# screen.listen()
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="a", fun=counter_clockwise)
# screen.onkey(key="d", fun=clockwise)
# screen.onkey(key="c", fun=clear)
# screen.exitonclick()
all_turtles = []
screen=Screen()
screen.bgcolor("black")
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make you bet",prompt="Which turtle will w"
                                                        "in the race?"
                                                        "Enter a Color:"
                                                        "'ROYGBP'")
colors  = ["red","orange","yellow","green","blue","purple"]
y=0


for x in colors:
    x = Turtle(shape="turtle")
    x.color(colors[y])
    x.penup()
    y += 1
    x.goto(x=-230,y=-100+y*30)
    all_turtles.append(x)

if  user_bet:
    still_on = True
winner=[]
while still_on:
    for turtle in all_turtles:
        if turtle.xcor()>210:
            still_on =  False
            winner.append(turtle)
            if len(winner)>1:
                print("Its a draw")
            elif user_bet ==  turtle.pencolor():
                print(f"You have won! The {turtle.pencolor()} turtle is the winner of the race!")
            else:
                print(f"You have lost! The {turtle.pencolor()} turtle is the winner of the race!")

        rand_distance = randint(0,31)
        turtle.forward(rand_distance)
screen.exitonclick()

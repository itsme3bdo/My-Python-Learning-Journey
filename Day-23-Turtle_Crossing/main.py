import time
from random import random, randint
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

score_board = Scoreboard()

playerr=Player()
screen.listen()
screen.onkey(playerr.up,"Up")

carz = []
for x in range(600):
    x = CarManager()
    carz.append(x)

can_go=[]
per_carz=150
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if playerr.reset():
        score_board.update_scoreboard()
        per_carz+=100
        for num in carz:
            num.incres()

    if randint(0,1000)<0+per_carz:
        can_go.append(carz[randint(0,599)])

    for n in can_go:
        n.arrive()
        if playerr.distance(n)<20:
            game_is_on=False
            score_board.gameover()

screen.exitonclick()


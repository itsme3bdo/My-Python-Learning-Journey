from scoreboard import Scoreboard
from snake import Snake
from turtle import Screen
import time
from food import Food

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Diddy Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on  = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    #detect collision with food
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.add_1()
    snake.move()
    #detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300  or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # detect collision with tail.
    for segment in snake.segments[1:]:
        if  snake.head.distance((segment)) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()

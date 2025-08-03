from turtle import Screen
from paddles import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Ping Ching Chong Game")
screen.tracer(0)

paddler_r=Paddle(350, 0)
paddle2_l=Paddle(-350, 0)
screen.listen()
screen.onkey(paddler_r.up, "Up")
screen.onkey(paddler_r.down, "Down")
screen.onkey(paddle2_l.up, "w")
screen.onkey(paddle2_l.down, "s")

ball = Ball()
scoreboard=Scoreboard()


game_on = True
while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    #detect collision with r_paddle
    if ball.ycor()>280 or  ball.ycor()<-280:
        ball.bounce_y()

    #detect collision with r_paddle
    if ball.distance(paddler_r)  <  50 and ball.xcor()>320 or ball.distance(paddle2_l) < 50 and  ball.xcor()<-320:
        ball.bounce_x()

    #detect when ball misses r paddle
    if ball.xcor()>380:
        ball.reseet()
        scoreboard.l_point()

    #detech when ball misses le paddle
    if ball.xcor() < -380:
        ball.reseet()
        scoreboard.r_point()


screen.exitonclick()

from turtle import *
import time

from scoreboard import Scoreboard

from ball import Ball
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

scoreboard = Scoreboard()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.change_position()

    # Detect collision with the upper or lower wall
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()

    # Detect collision with paddle
    if (ball.distance(r_paddle) < 52 and ball.xcor() > 330) or (ball.distance(l_paddle) < 52 and ball.xcor() < -330):
        ball.bounce_x()

    # Detect going behind the right paddle
    if ball.xcor() > 380:
        ball.restart_into_left()
        scoreboard.l_point()

    # Detect going behind the left paddle

    if ball.xcor() < -380:
        ball.restart_into_right()
        scoreboard.r_point()

screen.exitonclick()

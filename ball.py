from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 0)
        self.color("white")
        self.shape("circle")
        self.xcor_move = 10
        self.ycor_move = 10
        self.ball_speed = 0.1

    def change_position(self):
        self.goto(self.xcor() + self.xcor_move, self.ycor() + self.ycor_move)

    def bounce_y(self):
        self.ycor_move *= -1

    def bounce_x(self):
        self.xcor_move *= -1
        self.ball_speed *= 0.9

    def restart_into_right(self):
        self.goto(0, 0)
        self.xcor_move = 10
        self.ycor_move = 10
        self.ball_speed = 0.1

    def restart_into_left(self):
        self.goto(0, 0)
        self.xcor_move = -10
        self.ycor_move = 10
        self.ball_speed = 0.1

from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, coordinates_tuple):
        super().__init__()
        self.coordinates_tuple = coordinates_tuple
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(5, 1)
        self.goto(coordinates_tuple)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

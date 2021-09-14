from turtle import Turtle
X = 10
Y = 10


class Ball(Turtle):

    def __init__(self):
        super().__init__()

        self.color('white')
        self.shape('circle')
        self.x = 10
        self.y = 10
        self.penup()

    def move(self):
        x = self.xcor() + self.x
        y = self.ycor() + self.y
        self.goto(x, y)

    def bounce_y(self):
        self.y *= -1

    def bounce_x(self):
        self.x *= -1

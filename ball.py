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

    def move_up(self):
        x = self.xcor() + self.x
        y = self.ycor() + self.y
        self.goto(x, y)

    def move_down(self):
        self.y *= -1
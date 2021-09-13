import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title('Pong')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

ball = Ball()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    ball.move_up()

    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.move_down()

screen.exitonclick()

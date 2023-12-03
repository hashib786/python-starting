from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Hashib PONG Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Collision detection in Y direction
    if (ball.ycor() >= 280 or ball.ycor() <= -280):
        ball.y_bounce()

    # Collision detection in X direction
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.x_bounce()

    # Check wether ball is outside our screen
    if (ball.xcor() > 380 or ball.xcor() < -380):
        ball.reset_position()
        is_game_on = False
        screen.update()

screen.exitonclick()

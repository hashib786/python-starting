from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreBoard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Hashib PONG Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Collision detection in Y direction
    if (ball.ycor() >= 280 or ball.ycor() <= -280):
        ball.y_bounce()

    # Collision detection in X direction
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.x_bounce()

    # Check wether ball is outside our L-screen
    if (ball.xcor() > 380):
        scoreboard.l_point()
        ball.reset_position()

    # Check wether ball is outside our R-screen
    if (ball.xcor() < -380):
        scoreboard.r_point()
        ball.reset_position()

screen.exitonclick()

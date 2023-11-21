from turtle import Turtle, Screen
from random import randint
import turtle as t

timmy = Turtle()
t.colormode(255)
timmy.shape("turtle")

timmy.color("black")
timmy.fillcolor("green")

# for _ in range(4):
#     timmy.forward(100)
#     timmy.left(90)

# for _ in range(50):
#     timmy.forward(5)
#     timmy.pencolor("white")
#     timmy.forward(5)
#     timmy.pencolor("black")


def random_color():
    return (randint(0, 255), randint(0, 255), randint(0, 255))


timmy.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)


draw_spirograph(5)

myScreen = Screen()
myScreen.exitonclick()

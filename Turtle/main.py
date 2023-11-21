from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")

timmy.color("red")
timmy.fillcolor("green")

for _ in range(4):
    timmy.forward(100)
    timmy.left(90)

myScreen = Screen()
myScreen.exitonclick()

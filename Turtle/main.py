from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")

timmy.color("black")
timmy.fillcolor("green")

# for _ in range(4):
#     timmy.forward(100)
#     timmy.left(90)

for _ in range(50):
    timmy.forward(5)
    timmy.pencolor("white")
    timmy.forward(5)
    timmy.pencolor("black")

myScreen = Screen()
myScreen.exitonclick()

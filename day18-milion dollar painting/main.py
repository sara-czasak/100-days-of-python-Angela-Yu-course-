from turtle import Turtle, Screen
import random
from turtle_helper_functions import *

screen = Screen()
screen.colormode(255)

turtle = Turtle()
turtle.hideturtle()

turtle.penup()
turtle.goto(-290,-245)
turtle.speed(0)


row = 1

for i in range(14):
    for j in range(15):
        R, G, B = change_color()
        turtle.color(R, G, B)

        turtle.pendown()
        turtle.dot(size=28)
        turtle.up()
        turtle.forward(38)

        row += 1
    if row % 2 == 0:
        even_row(turtle)
    else:
        odd_row(turtle)










screen.exitonclick()


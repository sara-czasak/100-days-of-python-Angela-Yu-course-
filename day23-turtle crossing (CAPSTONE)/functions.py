from turtle import Turtle
import random


def board_setup():
    t = Turtle()
    t.speed(0)
    t.hideturtle()
    t.pensize(3)
    t.up()
    t.goto(0, -240)
    t.down()
    t.setheading(90)
    for i in range(13):
        t.forward(20)
        t.up()
        t.forward(20)
        t.down()


def change_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b
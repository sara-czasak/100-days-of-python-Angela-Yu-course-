from turtle import Turtle


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

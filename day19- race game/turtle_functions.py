import turtle
import random


def move():
    turtle.forward(10)


def turn_right():
    turtle.right(10)


def turn_left():
    turtle.left(10)


def setup_race_track(t):
    t.penup()
    t.hideturtle()
    t.speed(0)
    t.goto(-320, -240)

    # Setup initial race board
    t.left(90)
    t.pensize(4)
    for i in range(13):
        t.pendown()
        t.forward(20)
        t.penup()
        t.forward(20)

    t.goto(-400, -160)

    for i in range(2):
        t.right(90)

        t.pendown()
        t.forward(800)
        t.penup()
        t.left(90)
        t.forward(80)
        t.left(90)

        t.pendown()
        t.forward(800)
        t.penup()
        t.right(90)
        t.forward(80)

    t.right(90)

    t.pendown()
    t.forward(800)


def change_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r, g, b


def setup_racers():
    x = -360
    y = -200
    colors = ['purple', 'blue', 'green', 'yellow', 'orange', 'red']
    racers = []
    for i in range(6):
        t = turtle.Turtle()
        t.turtlesize(3)
        t.shape("turtle")
        t.color(colors[i])
        t.penup()
        t.goto(x, y)
        racers.append(t)
        y += 80
    return racers


def random_distance():
    distance = random.randint(0,10)
    return distance


def check_if_finish(t, finish_line):
    if t.xcor() >= finish_line:
        return True
    else:
        return False


def check_bet(winner, bet_color):
    if winner == bet_color:
        return True
    else:
        return False

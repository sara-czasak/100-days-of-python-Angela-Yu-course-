import random


def change_color():
    R = random.randint(0,255)
    G = random.randint(0,255)
    B = random.randint(0,255)
    return (R,G,B)


def odd_row(turtle):
    R, G, B = change_color()
    turtle.color(R, G, B)
    turtle.dot(size=30)
    turtle.up()
    turtle.right(90)
    turtle.forward(38)
    turtle.right(90)


def even_row(turtle):
    R, G, B = change_color()
    turtle.color(R, G, B)
    turtle.dot(size=30)
    turtle.up()
    turtle.left(90)
    turtle.forward(38)
    turtle.left(90)
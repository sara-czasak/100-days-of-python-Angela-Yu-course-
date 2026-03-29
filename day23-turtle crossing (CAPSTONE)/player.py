from turtle import Turtle
from functions import *


# CONSTANTS
SPEED = 10


class Player(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.reset()
        self.speed = 10


    def move(self):
        self.goto(self.xcor(), self.ycor() + SPEED)


    def reset(self):
        self.shape("turtle")
        self.color("black", change_color())
        self.hideturtle()
        self.penup()
        self.setheading(90)
        self.turtlesize(2, outline=2)
        self.goto(self.x, self.y)
        self.showturtle()
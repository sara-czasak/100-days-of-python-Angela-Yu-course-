from turtle import Turtle
from functions import *


# CONSTANTS
SPEED = 10


class Player(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.create_player()
        self.speed = 10


    def create_player(self):
        self.shape("turtle")
        self.color(change_color())
        self.hideturtle()
        self.penup()
        self.setheading(90)
        self.turtlesize(2)
        self.goto(self.x, self.y)
        self.showturtle()


    def move(self):
        self.goto(self.xcor(), self.ycor() + SPEED)
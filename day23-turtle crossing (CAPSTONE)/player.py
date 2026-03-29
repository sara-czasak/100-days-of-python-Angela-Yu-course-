from turtle import Turtle
from functions import *


# CONSTANTS
SPEED = 5
FINISH_LINE = 180


class Player(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.player_color = change_color()
        self.reset()
        self.speed = 10


    def move(self):
        self.goto(self.xcor(), self.ycor() + SPEED)


    def reset(self):
        self.penup()
        self.shape("turtle")
        self.color("black", self.player_color)
        self.hideturtle()

        self.setheading(90)
        self.turtlesize(1.5, outline=1.5)
        self.goto(self.x, self.y)
        self.showturtle()


    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE:
            return True
        else:
            return False
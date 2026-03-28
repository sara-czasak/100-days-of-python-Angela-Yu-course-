from turtle import Turtle
from functions import *
import random

# CONSTANTS
SPEED = 2


class Cars(Turtle):
    def __init__(self):
        super().__init__()
        x = 420
        # y = random.randint(-100, 200)
        self.new_car(x, random.randint(-100, 200))
        self.cars = []

    def new_car(self, x, y):
        cars = []
        for i in range(10):
            self.shape("square")
            self.color(change_color())
            self.shapesize(1.5, 4)
            self.penup()
            self.hideturtle()
            self.goto(x, random.randint(-100, 200))
            self.setheading(180)
            self.showturtle()
            self.move()
            cars.append(Cars())
        return cars

    def move(self):
        while self.xcor() > -320:
            self.forward(SPEED)
        else:
            self.hideturtle()
        # self.goto(self.xcor() + SPEED, self.ycor())
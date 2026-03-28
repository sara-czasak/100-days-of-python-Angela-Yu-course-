from turtle import Turtle
import random
from func import *


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.food_x = random.randint(-280, 280)
        self.food_y = random.randint(-280, 280)


    def new_food(self):
        food = Turtle()
        food.hideturtle()
        food.penup()
        food.goto((self.food_x, self.food_y))
        food.color(change_color())
        food.shape('circle')
        food.turtlesize(0.5)
        food.showturtle()



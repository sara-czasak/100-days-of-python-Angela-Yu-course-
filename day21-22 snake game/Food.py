from turtle import Turtle
import random
from func import *


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.refresh()


    def refresh(self):
        random_x = random.randint(-260, 260)
        random_y = random.randint(-260, 260)
        self.goto(random_x, random_y)
        color = change_color()
        self.color(color)

if __name__ == '__main__':
    print("You are currently in the Food module. Please run main.py file.")
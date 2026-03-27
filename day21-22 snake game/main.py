from Snake import *
from turtle import Turtle, Screen
from func import *

screen = Screen()
screen.setup(500,500)
screen.colormode(255)

snake = Snake()

play_snake = True
moving = False

while True:
    snake.move(moving)
    moving = True






screen.exitonclick()
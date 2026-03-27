from turtle import Turtle, Screen
import time
from Snake import Snake


screen = Screen()
screen.setup(width=600, height=600)
screen.colormode(255)
screen.bgcolor("black")
screen.title("Snake Game v1")
screen.tracer(0)

snake = Snake()
screen.update()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

screen.exitonclick()
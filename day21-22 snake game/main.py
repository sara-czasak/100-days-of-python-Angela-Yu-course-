from turtle import Turtle, Screen
import time
from func import *


screen = Screen()
screen.setup(width=600, height=600)
screen.colormode(255)
screen.bgcolor("black")
screen.title("Snake Game v1")
screen.tracer(0)

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in starting_positions:
    new_segment = Turtle('circle')
    new_segment.penup()


    new_segment.goto(position)
    if new_segment.position() == (0, 0):
        new_segment.color('white')
    else:
        new_segment.color(change_color())
    segments.append(new_segment)

screen.update()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num-1].xcor()
        new_y = segments[seg_num-1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)

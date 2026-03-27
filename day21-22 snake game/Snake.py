from turtle import Turtle
from func import *


# CONSTANTS
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_initial_snake_body()
        self.head = self.segments[0]


    def create_initial_snake_body(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle('circle')
            new_segment.penup()

            new_segment.goto(position)
            if new_segment.position() == (0, 0):
                new_segment.color('white')
            else:
                new_segment.color(change_color())
            self.segments.append(new_segment)


    def move_snake(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)


    def check_valid_move(self, current_heading, move_direction):
        print("current dir: ",current_heading)
        print("new dir: ", move_direction)
        if current_heading != move_direction:
            return True
        else:
            return False


    def move_left(self):
        if not self.head.heading() == 0.0:
            self.head.setheading(180)


    def move_right(self):
        if not self.head.heading() == 180:
            self.head.setheading(0)


    def move_up(self):
        if not self.head.heading() == 270:
            self.head.setheading(90)


    def move_down(self):
        if not self.head.heading() == 90:
            self.head.setheading(270)

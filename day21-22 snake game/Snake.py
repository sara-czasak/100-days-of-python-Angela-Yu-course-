from turtle import Turtle
from func import *
from Food import Food


# CONSTANTS
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_initial_snake_body()
        self.head = self.segments[0]
        self.tail = self.segments[-1]

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
        if not self.head.heading() == RIGHT:
            self.head.setheading(LEFT)


    def move_right(self):
        if not self.head.heading() == LEFT:
            self.head.setheading(RIGHT)


    def move_up(self):
        if not self.head.heading() == DOWN:
            self.head.setheading(UP)


    def move_down(self):
        if not self.head.heading() == UP:
            self.head.setheading(DOWN)


    def eat_food(self):
        print("EATING FOOD")


if __name__ == '__main__':
    print("You are currently in the Snake module. Please run main.py file.")
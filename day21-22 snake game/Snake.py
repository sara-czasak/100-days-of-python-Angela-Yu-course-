from turtle import Turtle
from func import *


class Snake:
    def __init__(self):
        self.body = self.create_initial_body()
        self.head = self.body[-1]


    def create_initial_body(self):
        snake = []
        x = -20
        y = 0
        for i in range(3):
            t = Turtle()
            t.penup()
            t.shape('circle')
            t.goto(x, y)
            if i == 2:
                t.color('black')
            else:
                t.color(change_color())
            x += 20
            snake.append(t)
        return snake


    def move(self, moving):
        if moving == True:
            for i in  self.body:
                i.forward(5)
        else:
            for i in self.body:
                i.setheading(0)


    def change_direction(self, direction):
        last_segment = self.head.pos()
        for segment in self.body:
            if last_segment == self.body[-1]:
                if direction == 'up':
                    segment.setheading(90)
                    segment.forward(5)
                else:
                    current_pos = segment.pos()
                    segment.goto(last_segment)
                    last_segment = current_pos

        # if direction == 'up':
        #     for i in self.body:
        #         if i == self.head:
        #             i.setheading(90)
        #             i.forward(5)






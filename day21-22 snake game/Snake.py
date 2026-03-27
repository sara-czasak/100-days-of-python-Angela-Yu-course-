from turtle import Turtle
from func import *


class Snake:
    def __init__(self):
        self.body = self.create_initial_body()
        self.head = self.body[-1]
        self.segments = []
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]

    def create_initial_body(self):
        for position in self.starting_positions:
            t = Turtle()
            t.penup()
            t.shape('circle')
            t.goto(position)
            if position == (0, 0):
                t.color('black')
            else:
                t.color(change_color())
            self.segments.append(t)
        return self.segments


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






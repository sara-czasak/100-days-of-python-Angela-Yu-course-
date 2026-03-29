from turtle import Turtle
from functions import change_color
import random


# CONSTANTS
STARTING_POSITIONS = [(400, -25), (400, -75), (400, -125), (400, 25), (400, 75), (400, 125)]
MOVE_DISTANCE = 1
CAR_DISTANCE = 100


class Car(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.all_cars = []

    def create_car(self):
        new_car = Turtle()
        new_car.penup()
        new_car.hideturtle()
        new_car.shape("square")
        new_car.shapesize(1, 4, outline=2)
        new_car.color(change_color(), change_color())
        new_car.goto(random.choice(STARTING_POSITIONS))
        new_car.setheading(180)

        if self.lane_clear(new_car):
            new_car.showturtle()
            self.all_cars.append(new_car)
        else:
            pass

    def move(self):
        for car in self.all_cars:
            new_x = car.xcor() - MOVE_DISTANCE
            car.goto(new_x, car.ycor())
            if car.xcor() < -350:
                car.hideturtle()
                car.goto(random.choice(STARTING_POSITIONS))


    def lane_clear(self, new_car):
        for car in self.all_cars:
            distance = car.distance(new_car)
            if distance < CAR_DISTANCE:
                return False
        return True


    def reset(self, car_to_reset):
        self.hideturtle()
        self.goto(random.choice(STARTING_POSITIONS))
        self.showturtle()
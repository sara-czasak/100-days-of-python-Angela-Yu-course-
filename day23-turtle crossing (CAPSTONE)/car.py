from turtle import Turtle
from functions import change_color
import random


# CONSTANTS
LANE_Y_POSITIONS = [-25, -75, -125, 25, 75, 125]
CAR_DISTANCE = 5
SPEED_ICREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = CAR_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 12)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.hideturtle()
            new_car.shapesize(stretch_wid=2, stretch_len=4, outline=5)
            new_car.penup()
            new_car.color(change_color(), change_color())
            random_y = random.choice(LANE_Y_POSITIONS)
            new_car.goto(400, random_y)
            # new_car.setheading(180)
            if self.lane_clear(new_car):
                new_car.showturtle()
                self.all_cars.append(new_car)


    def move_cars(self):
        for car in self.all_cars:
            car.backward(CAR_DISTANCE)


    def lane_clear(self, new_car):
        for car in self.all_cars:
            if abs(car.ycor() - new_car.ycor()) < 40:
                return False
        return True


    def level_up(self):
        self.car_speed += SPEED_ICREMENT
#
# class Car(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.all_cars = []
#
#
#     def create_car(self):
#             x = random.randint(200, 800)
#             y = random.choice(LANE_Y_POSITIONS)
#             new_car = Turtle()
#             new_car.penup()
#             new_car.hideturtle()
#             new_car.shape("square")
#             new_car.shapesize(1, 4, outline=2)
#             new_car.color(change_color(), change_color())
#             new_car.goto(x, y)
#             new_car.setheading(180)
#
#             if self.lane_clear(new_car):
#                 new_car.goto(430, new_car.ycor())
#                 new_car.showturtle()
#                 self.all_cars.append(new_car)
#             else:
#                 pass
#
#     def move(self):
#         for car in self.all_cars:
#             new_x = car.xcor() - random.randint(1, MAX_SPEED)
#             car.goto(new_x, car.ycor())
#             if car.xcor() < -430:
#                 car.hideturtle()
#                 self.reset_car(car)
#
#
#     def lane_clear(self, new_car):
#         for car in self.all_cars:
#             if abs(car.ycor() - new_car.ycor()) < 40:
#                 return False
#         return True
#
#
#     def reset_car(self, car):
#         y = random.choice(LANE_Y_POSITIONS)
#         car.goto(430, y)
#         car.color(change_color(), change_color())
#         car.showturtle()
#

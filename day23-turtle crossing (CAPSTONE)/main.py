from turtle import Screen
from player import Player
from car import Car
import time
from canv import *


screen = Screen()
screen.setup(width=800, height=500)
screen.bgcolor("white")
screen.colormode(255)
screen.title("*** Turtle Crossing ***")
screen.listen()

bg = BackGround()

player = Player(0, -200)
car = Car()

max_cars = 10

game_on = True
while game_on:
    screen.update()

    if len(car.all_cars) < max_cars:
        car.create_car()
        car.move()
    time.sleep(0.001)
    screen.onkeypress(player.move, "space")
    if player.ycor() > 180:
        player.reset()
    for i in car.all_cars:
        if i.distance(player) < 50:
            player.reset()
            game_on = False




screen.exitonclick()
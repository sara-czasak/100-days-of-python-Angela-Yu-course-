from turtle import Screen
from player import Player
from car import CarManager
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
car_manager = CarManager()


game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    screen.onkeypress(player.move, "space")

    for car in car_manager.all_cars:
        if car.distance(player) < 40:
            game_on = False

    if player.is_at_finish_line():
        player.reset()
        car_manager.level_up()



screen.exitonclick()
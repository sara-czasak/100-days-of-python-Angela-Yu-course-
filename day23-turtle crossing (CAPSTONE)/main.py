from turtle import Screen
from player import Player
from car import CarManager
import time
from canv import *
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width=800, height=500)
screen.bgcolor("white")
screen.colormode(255)
screen.title("*** Turtle Crossing ***")
screen.listen()

scoreboard = ScoreBoard()
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
            scoreboard.game_over()
            game_on = False

    if player.is_at_finish_line():
        player.reset()
        scoreboard.increase_score()
        car_manager.level_up()



screen.exitonclick()
from turtle import Turtle, Screen
from player import Player
import time
from car import Cars

screen = Screen()
screen.setup(width=800, height=500)
screen.bgcolor("white")
screen.colormode(255)
screen.title("*** Turtle Crossing ***")
screen.listen()

player = Player(0, -220)


game_on = True
while game_on:
    screen.update()
    time.sleep(0.01)
    screen.onkey(player.move, "space")
    cars = Cars()




screen.exitonclick()
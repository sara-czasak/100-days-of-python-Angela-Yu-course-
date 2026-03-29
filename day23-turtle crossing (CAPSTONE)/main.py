from turtle import Turtle, Screen
from player import Player
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

game_on = True
while game_on:
    screen.update()
    time.sleep(0.01)
    screen.onkey(player.move, "space")
    if player.ycor() > 180:
        player.reset()


screen.exitonclick()
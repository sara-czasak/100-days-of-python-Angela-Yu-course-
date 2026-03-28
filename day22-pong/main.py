from turtle import Screen
from functions import *
from Paddle import Paddle

screen = Screen()
screen.setup(800, 500)
screen.title("*** Pong ***")
board_setup()

paddle1 = Paddle(350, 0)
paddle2 = Paddle(-350, 0)

screen.listen()
screen.onkeypress(paddle1.up, "Up")
screen.onkeypress(paddle1.down, "Down")
screen.onkeypress(paddle2.up, "w")
screen.onkeypress(paddle2.down, "s")

screen.exitonclick()
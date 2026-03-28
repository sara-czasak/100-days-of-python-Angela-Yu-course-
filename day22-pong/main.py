from turtle import Screen
from functions import *
from Paddle import Paddle
from Ball import *
import time
from ScoreBoard import *

screen = Screen()
screen.setup(800, 500)
screen.title("*** Pong ***")
board_setup()

paddle_r = Paddle(350, 0)
paddle_l = Paddle(-350, 0)

ball = Ball()

score1 = 0
score2 = 0
scoreboard = ScoreBoard(score1, score2)

screen.listen()
screen.onkeypress(paddle_r.up, "Up")
screen.onkeypress(paddle_r.down, "Down")
screen.onkeypress(paddle_l.up, "w")
screen.onkeypress(paddle_l.down, "s")


game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    # Detect wall collision
    if ball.ycor() > 240 or ball.ycor() < -240:
        ball.bounce_y()

    # Detect paddle collision
    if ball.distance(paddle_r) < 50 and ball.xcor() > -420 or ball.distance(paddle_l) < 50 and ball.xcor() < 420:
        ball.bounce_x()


    # Detect ball out of bounds
    if ball.xcor() > 380:
        score1 += 1
        scoreboard.update_score(score1, score2)
        ball.reset_ball()

    if ball.xcor() < -380:
        score2 += 1
        scoreboard.update_score(score1, score2)
        ball.reset_ball()





screen.exitonclick()
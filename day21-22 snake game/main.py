from turtle import Turtle, Screen
import time
from Snake import Snake
from Food import Food
from ScoreBoard import ScoreBoard


screen = Screen()
screen.setup(width=600, height=600)
screen.colormode(255)
screen.bgcolor("black")
screen.title("Snake Game v1")
screen.tracer(0)

score = 0

snake = Snake()
food = Food()
scoreboard = ScoreBoard(score)

screen.listen()
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")
screen.onkey(snake.move_up,"Up")



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    # Detect collision with food
    if snake.head.distance(food) < 20:
        snake.eat_food()
        food.refresh()
        score += 1
        scoreboard.update_score(score)


    # Detect collision with screen edges
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        game_is_on = False



screen.exitonclick()
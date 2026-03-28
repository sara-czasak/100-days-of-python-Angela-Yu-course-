from turtle import Turtle, Screen
import time
from Snake import Snake
from Food import Food


screen = Screen()
screen.setup(width=600, height=600)
screen.colormode(255)
screen.bgcolor("black")
screen.title("Snake Game v1")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")
screen.onkey(snake.move_up,"Up")

food = Food()


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    food.new_food()

screen.exitonclick()
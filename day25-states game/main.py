from turtle import Turtle, Screen
from quiz_brain import *

screen = Screen()
screen.title("USA States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle = Turtle()
turtle.shape(image)

play = True

while play:
    answer = screen.textinput('Guess a state', 'What is your guess?')

    if answer.lower() == 'done':
        play = False
    else:
        coors = check_if_state(answer)
        if type(coors) == tuple:
            state_turtle = Turtle()
            state_turtle.hideturtle()
            state_turtle.up()
            state_turtle.goto(coors[0], coors[1])
            state_turtle.down()
            state_turtle.write(answer.capitalize())

screen.mainloop()
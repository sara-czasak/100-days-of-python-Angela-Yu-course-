from turtle import Turtle, Screen
from quiz_brain import *

screen = Screen()
screen.title("USA States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle = Turtle()
turtle.shape(image)

play = True

count = 0
guessed_states = []

while play:
    answer = screen.textinput(f'{count}/50 States Correct', 'What is your guess?')

    if answer.lower() == 'done':
        missed_states(guessed_states)
        play = False
    else:
        coors = check_if_state(answer)
        if type(coors) == tuple and answer.capitalize() not in guessed_states:
            state_turtle = Turtle()
            state_turtle.hideturtle()
            state_turtle.up()
            state_turtle.goto(coors[0], coors[1])
            state_turtle.down()
            state_turtle.write(answer.capitalize())
            guessed_states.append(answer.capitalize())
            count += 1

screen.mainloop()
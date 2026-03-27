from turtle import Turtle, Screen
from turtle_functions import *

screen = Screen()
screen.setup(800,500)
screen.colormode(255)

finish_line = 390

t = Turtle()
setup_race_track(t)

racers = setup_racers()

colors = ['purple', 'blue', 'green', 'yellow', 'orange', 'red']
bet = turtle.textinput("Bet color", "*** Which turtle would you like to bet on? ***")
bet_placed = False
while not bet_placed:
    if bet not in colors:
        bet = turtle.textinput("Bet color", "!!! INVALID SELECTION TRY AGAIN !!!\n*** Which turtle would you like to bet on? ***")
    else:
        bet_placed = True





racing = True

while racing:
    for racer in racers:
        racer.forward(random_distance())
        if check_if_finish(racer, finish_line):
            winner = racer.color()[0]
            racing = False
print(f"The winner is the {winner.capitalize()} Turtle!")
if check_bet(winner, bet):
    turtle.hideturtle()
    turtle.write("You won!", font=("Arial", 20, "bold"))
else:
    turtle.hideturtle()
    turtle.write(f"You lost!\n *** {winner.capitalize()} Turtle won! ***", font=("Arial", 20, "bold"))



screen.exitonclick()


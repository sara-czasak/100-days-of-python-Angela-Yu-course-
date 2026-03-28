from turtle import Turtle


# CONSTANTS
FONT = ("Courier", 24, "bold")
ALIGN = "center"
COLOR = 'black'


class ScoreBoard(Turtle):
    def __init__(self, score1, score2):
        super().__init__()
        self.color(COLOR)
        self.penup()
        self.hideturtle()
        self.goto(0, 210)
        text = f"PLAYER 1: {score1}   PLAYER 2: {score2}"
        self.write(text, align=ALIGN, font=FONT)


    def update_score(self, score1, score2):
        self.reset()
        text = f"PLAYER 1: {score1}   PLAYER 2: {score2}"
        self.color(COLOR)
        self.penup()
        self.hideturtle()
        self.goto(0, 210)
        text = f"PLAYER 1: {score1}   PLAYER 2: {score2}"
        self.write(text, align=ALIGN, font=FONT)



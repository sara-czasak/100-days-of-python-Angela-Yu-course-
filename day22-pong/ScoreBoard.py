from turtle import Turtle


# CONSTANTS
FONT = ("Courier", 40, "bold")
ALIGN = "center"
COLOR = 'black'


class ScoreBoard(Turtle):
    def __init__(self, score1, score2):
        super().__init__()
        self.color(COLOR)
        self.penup()
        self.hideturtle()
        self.goto(0, 190)
        text = f"{score1} {score2}"
        self.write(text, align=ALIGN, font=FONT)


    def update_score(self, score1, score2):
        self.clear()
        self.color(COLOR)
        self.penup()
        self.hideturtle()
        self.goto(0, 190)
        text = f"{score1} {score2}"
        self.write(text, align=ALIGN, font=FONT)

if __name__ == '__main__':
    print("This is the ScoreBoard module")

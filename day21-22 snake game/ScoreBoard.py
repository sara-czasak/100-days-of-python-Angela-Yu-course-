from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self, score):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        text = f"Score: {score}"
        self.write(text, align="center", font=("Courier", 24, "bold"))

    def update_score(self, score):
        self.reset()
        text = f"Score: {score}"
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        text = f"Score: {score}"
        self.write(text, align="center", font=("Courier", 24, "bold"))

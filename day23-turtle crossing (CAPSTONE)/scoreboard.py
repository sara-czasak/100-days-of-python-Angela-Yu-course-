from turtle import Turtle


FONT = ("Courier", 24, "bold")


class ScoreBoard:
    def __init__(self):
        self.score = 0
        self.writer = Turtle()
        self.create_score()

    def create_score(self):
        score_text = f"Score: {self.score}"
        self.writer.hideturtle()
        self.writer.penup()
        self.writer.goto(-350, 200)
        self.writer.pendown()
        self.writer.write(score_text, font=FONT)


    def increase_score(self):
        self.score += 1
        self.writer.clear()
        self.create_score()


    def game_over(self):
        self.writer.clear()
        game_over_text = f"***GAME OVER ***\nSCORE: {self.score}"
        self.writer.hideturtle()
        self.writer.penup()
        self.writer.goto(-100, 0)
        self.writer.pendown()
        self.writer.pencolor("red")
        self.writer.write(game_over_text, font=FONT)


from turtle import Turtle


# CONSTANTS
FONT = ("Courier", 24, "bold")
ALIGN = "center"
COLOR = 'white'

class ScoreBoard(Turtle):
    def __init__(self, score, high_score):
        super().__init__()
        self.high_score = high_score
        self.text2 = f"High Score: {self.high_score}"
        self.color(COLOR)
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        text = f"Score: {score}"
        self.write(text, align=ALIGN, font=FONT)
        self.goto(0, 220)
        self.write(self.text2, align=ALIGN, font=FONT)

    def update_score(self, score):
        self.reset()
        text = f"Score: {score}"
        self.color(COLOR)
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        text = f"Score: {score}"

        self.write(text, align=ALIGN, font=FONT)
        self.goto(0, 220)
        self.write(self.text2, align=ALIGN, font=FONT)


    def game_over_text(self, score):
        self.reset()
        self.color(COLOR)
        if score > self.high_score:
            self.high_score = score
        self.write(f"GAME OVER\nYOUR SCORE: {score}\nHIGH SCORE: {self.high_score}", align=ALIGN, font=FONT)



if __name__ == '__main__':
    print("You are currently in the ScoreBoard module. Please run main.py file.")
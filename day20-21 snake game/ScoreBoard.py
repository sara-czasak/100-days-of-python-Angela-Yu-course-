from turtle import Turtle


# CONSTANTS
FONT = ("Courier", 24, "bold")
ALIGN = "center"
COLOR = 'white'

class ScoreBoard(Turtle):
    def __init__(self, score):
        super().__init__()
        self.color(COLOR)
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        text = f"Score: {score}"
        self.write(text, align=ALIGN, font=FONT)

    def update_score(self, score):
        self.reset()
        text = f"Score: {score}"
        self.color(COLOR)
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        text = f"Score: {score}"
        self.write(text, align=ALIGN, font=FONT)


    def game_over_text(self, score):
        self.reset()
        self.color(COLOR)
        self.write(f"GAME OVER\nYOUR SCORE IS: {score}", align=ALIGN, font=FONT)



if __name__ == '__main__':
    print("You are currently in the ScoreBoard module. Please run main.py file.")
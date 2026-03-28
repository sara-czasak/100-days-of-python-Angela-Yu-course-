from turtle import Turtle


# CONSTANTS
MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.create_paddle()


    def create_paddle(self):
        self.shape("square")
        self.penup()
        self.goto(self.x, self.y)
        self.shapesize(5, 1)


    def up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)


    def down(self):
        self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)



if __name__ == '__main__':
    print("This is the Paddle module")
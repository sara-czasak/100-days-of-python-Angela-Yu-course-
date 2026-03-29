from turtle import Turtle


class BackGround(Turtle):
    def __init__(self):
        Turtle.__init__(self)

        self.speed(0)
        self.hideturtle()

        # Draw lanes
        self.shape("square")
        self.color("black")
        self.penup()
        self.setheading(180)
        self.goto(400, -150)
        self.pendown()
        self.pensize(4)
        self.forward(800)

        self.penup()
        self.pensize(2)
        self.goto(400, -100)
        self.pendown()
        self.setheading(180)
        self.forward(800)

        self.penup()
        self.goto(400, -50)
        self.pendown()
        self.setheading(180)
        self.forward(800)

        self.penup()
        self.goto(400, 0)
        self.pendown()
        self.setheading(180)
        self.forward(800)

        self.penup()
        self.goto(400, 50)
        self.pendown()
        self.setheading(180)
        self.forward(800)

        self.penup()
        self.goto(400, 100)
        self.pendown()
        self.setheading(180)
        self.forward(800)

        self.penup()
        self.pensize(4)
        self.goto(400, 150)
        self.pendown()
        self.setheading(180)
        self.forward(800)


        # Draw zebra crossing

        self.pencolor("gray")
        self.penup()
        self.pensize(6)

        pos_y = -140
        done = False
        while not done:
            self.penup()
            self.goto(-50, pos_y)
            self.pendown()
            self.setheading(0)
            self.forward(100)
            pos_y += 10
            if pos_y > 140:
                done = True

            self.penup()



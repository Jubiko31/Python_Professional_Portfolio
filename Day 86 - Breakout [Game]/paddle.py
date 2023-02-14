from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("#1560DB")
        self.right(90)
        self.shapesize(stretch_wid=10, stretch_len=1)
        self.penup()
        self.goto(position)
    
    def go_right(self):
        if self.xcor() < 325:
            self.setx(self.xcor() + 80)

    def left(self):
        if self.xcor() > -325:
            self.setx(self.xcor() - 80)
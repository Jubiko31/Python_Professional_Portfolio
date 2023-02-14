from turtle import Turtle
from random import choice

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("lightgray")
        self.shape("circle")
        self.up()
        self.dx = choice((-15,-14,14,15))
        self.dy = choice((-16,-15,-14,14,15,16))

    def move(self):
        self.goto(self.xcor() + self.dx, self.ycor() + self.dy)
    
    def bounce(self):
        if self.ycor() > 360 or self.ycor() < -360:
            self.dy *= -1
        if self.xcor() > 490 or self.xcor() < -490:
            self.dx *= -1
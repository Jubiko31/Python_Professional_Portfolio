COLORS = ['#FAEBD7', '#76EEC6', '#E3CF57', '#8B7D6B', '#0000EE', '#FF4040', '#66CD00', '#FF7256', '#4D4D4D', '#DAA520']
X_POS = [x for x in range(-460, 500, 100)]
Y_POS = [y for y in range(100, 300, 30)]

from turtle import Turtle
from random import choice

class Block(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color(choice(COLORS))
        self.up()
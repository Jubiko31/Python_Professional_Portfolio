from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(400, 278)
        self.write(self.score, align="center", font=("Courier", 50, "normal"))

    def point(self):
        self.score += 1
        self.update_score()
        
    def end(self, user_score):
        self.clear()
        self.goto(0,0)
        self.write(f'\nGAME OVER\nScore: {user_score}', align="center", font=("Courier", 80, "normal"))

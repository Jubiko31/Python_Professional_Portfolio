from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from blocks import Block, Y_POS, X_POS
from time import sleep

screen = Screen()
screen.bgcolor("black")
screen.setup(width=980, height=720)
screen.title("Breakout Game")
screen.tracer(0)

paddle = Paddle((0, -300))
ball = Ball()
scoreboard = Scoreboard()
block_list = []

for y in Y_POS:
    for x in X_POS:
        block = Block()
        block.goto(x,y)
        block_list.append(block)

count = len(block_list)

screen.listen()
screen.onkey(paddle.left, "Left")
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.left, "a")
screen.onkey(paddle.go_right, "d")    

def collision_with_paddle():
    if ball.ycor() <= -280 and ball.ycor() >= -360 and ball.dy < 0:
        if ball.xcor()-10 <= paddle.xcor() + 100 and ball.xcor() +10 >= paddle.xcor()-100:
            ball.dy *= -1

def break_block():
    global count
    for block in block_list:
        if ball.xcor() + 10 >= block.xcor() - 60 and ball.xcor() - 10 <= block.xcor() + 60:
            if ball.ycor() >= block.ycor() - 20 and ball.ycor() <= block.ycor() + 20:
                ball.dy *= -1
                block.goto(1000,1000)
                scoreboard.point()
                count -= 1
                
while count > 0:
    sleep(0.1)
    screen.update()
    ball.move()
    # Check border collision
    ball.bounce()
    # Check for contact with paddle
    if ball.ycor() <= -350:
        count = 0
        break
    collision_with_paddle()
    # Break 'em!
    break_block()

if count <= 0:
    scoreboard.end(scoreboard.score)

screen.mainloop()
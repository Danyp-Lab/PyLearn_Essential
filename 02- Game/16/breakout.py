# Breakout Game in Python

import turtle

# Set up the screen
wn = turtle.Screen()
wn.title("Breakout Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)

# Paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=6)
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# Score
score = 3


# Functions to move paddle
def paddle_left():
    x = paddle.xcor()
    x -= 20
    paddle.setx(x)


def paddle_right():
    x = paddle.xcor()
    x += 20
    paddle.setx(x)


# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_left, "Left")
wn.onkeypress(paddle_right, "Right")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.xcor() > 290:
        ball.setx(290)
        ball.dx *= -1

    if ball.xcor() < -290:
        ball.setx(-290)
        ball.dx *= -1

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.goto(0, 0)
        ball.dy *= -1
        score -= 1
        if score == 0:
            print("Game Over")
            break

    # Paddle and ball collisions
    if (ball.ycor() < -240 and ball.ycor() > -250) and (
        ball.xcor() < paddle.xcor() + 50 and ball.xcor() > paddle.xcor() - 50
    ):
        ball.sety(-240)
        ball.dy *= -1

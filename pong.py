import turtle

teamBlue_score = 0
teamPink_score = 0

screen = turtle.Screen()
screen.title("2P Ping Pong")
screen.bgcolor('black')
screen.setup(width=800, height=600)
# screen.tracer(0)

leftPaddle = turtle.Turtle()
leftPaddle.speed(0)
leftPaddle.shape('square')
leftPaddle.color('skyblue')
leftPaddle.shapesize(stretch_wid=7, stretch_len=1)
leftPaddle.penup()
leftPaddle.goto(-350, 0)

rightPaddle = turtle.Turtle()
rightPaddle.speed(0)
rightPaddle.shape('square')
rightPaddle.shapesize(stretch_wid=7, stretch_len=1)
rightPaddle.color('pink')
rightPaddle.penup()
rightPaddle.goto(350, 0)

pen = turtle.Turtle()
pen.speed(0)
pen.color('red')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Team Blue: 0            Team Pink: 0", align="center", font=("candara", 24, "bold"))


# def leftPaddle_up():
#     y = leftPaddle.ycor()
#     y = y + 30
#     leftPaddle.sety(y)
#
#
# def leftPaddle_down():
#     y = leftPaddle.ycor()
#     y = y - 30
#     leftPaddle.sety(y)
#
#
# def rightPaddle_up():
#     y = rightPaddle.ycor()
#     y = y + 30
#     rightPaddle.sety(y)
#
#
# def rightPaddle_down():
#     y = rightPaddle.ycor()
#     y = y - 30
#     rightPaddle.sety(y)
#
#
# screen.listen()
# screen.onkeypress(leftPaddle_up, "w")
# screen.onkeypress(leftPaddle_down, "s")
# screen.onkeypress(rightPaddle_up, "Up")
# screen.onkeypress(rightPaddle_down, "Down")


turtle.mainloop()
#modules

import turtle
import time

#initialization

window = turtle.Screen()

window.title("ping pong")
window.bgcolor("black")
window.setup(width = 800, height = 600)
window.tracer(0)    

#paddles

def paddle(obj,x):
    obj.speed(0)
    obj.shape("square")
    obj.color("white")
    obj.shapesize(stretch_wid=5, stretch_len=1)
    obj.penup()
    obj.goto(x,0)

# on object

pad_a = turtle.Turtle()
paddle(pad_a,-350)

pad_b = turtle.Turtle()
paddle(pad_b,350)

#ball init

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)

#ball movement

ball.dx = 3
ball.dy = 3

#score

score_a = 0
score_b = 0

score = turtle.Turtle()
score.color("white")
score.penup()
score.goto(0, 260)
score.hideturtle()
score.write("Player A: 0  Player B: 0", align = "center", font = ("Courier", 24 ))
#up and down

#pad a

def pad_a_up():
    y = pad_a.ycor()
    y += 20
    pad_a.sety(y)

def pad_a_down():
    y = pad_a.ycor()
    y -= 20
    pad_a.sety(y)

#pad b

def pad_b_up():
    y = pad_b.ycor()
    y += 20
    pad_b.sety(y)

def pad_b_down():
    y = pad_b.ycor()
    y -= 20
    pad_b.sety(y)


#keyboard binding

window.listen()
window.onkeypress(pad_a_up, "w")
window.onkeypress(pad_a_down, "z")
window.onkeypress(pad_b_up, "i")
window.onkeypress(pad_b_down, "m")

#main loop

time.sleep(3)

while True:
    window.update()

    #ball movement

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #bounce

    if ball.ycor() > 290:           #top
        ball.dy *= -1

    if ball.ycor() < -280:          #bottom
        ball.dy *= -1

    if ball.xcor() > 380:           #right
        score_a += 1
        ball.goto(0,0)
        ball.dx *= -1

        score.clear()
        score.write(f"Player A: {score_a}  Player B: {score_b}", align = "center", font = ("Courier", 24 ))

    if ball.xcor() < -390:          #left
        score_b +=1
        ball.goto(0,0)
        ball.dx *= -1

        score.clear()
        score.write(f"Player A: {score_a}  Player B: {score_b}", align = "center", font = ("Courier", 24 ))

    #ball collision

    if ball.xcor() > 330 and ball.ycor() < (pad_b.ycor() + 55) and ball.ycor() > (pad_b.ycor() - 55):
        ball.dx *= -1

    if ball.xcor() < -330 and ball.ycor() < (pad_a.ycor() + 55) and ball.ycor() > (pad_a.ycor() - 55):
        ball.dx *= -1

    #restrict paddle
    if pad_a.ycor() > 250:
        pad_a.sety(250)

    if pad_a.ycor() < -250:
        pad_a.sety(-250)


    if pad_b.ycor() > 250:
        pad_b.sety(250)

    if pad_b.ycor() < -250:
        pad_b.sety(-250)


    

# modules

import turtle
import random


# right movement
def move_right():
    x = head.xcor()
    x += 20
    head.setx(x)
    head.seth(90)

# left movement
def move_left():
    x = head.xcor()
    x -= 20
    head.setx(x)
    head.seth(270)

# up movement
def move_up():
    y = head.ycor()
    y += 20
    head.sety(y)
    head.seth(0)

# down movement
def move_down():
    y = head.ycor()
    y -= 20
    head.sety(y)
    head.seth(180)

# initializing all turtle object's attributes
def object_frame(scrObj):
    scrObj.speed(0)
    scrObj.shape("square")
    scrObj.shapesize(stretch_wid = 0.9523 , stretch_len = 0.9523)
    scrObj.penup()

# initializing the snake 
def new_snake(scrObj):
    object_frame(scrObj)
    scrObj.color("white")
    scrObj.goto(0,0)
    scrObj._setmode(mode = "logo")

# Showing the food randomly
def show_food(foodObj):
    food_x = random.randrange(-380,380,20)
    food_y = random.randrange(-280,280,20)
    foodObj.goto(food_x,food_y)    


# if snake hits boundary, goes back to start
def check_boundary():
    if head.xcor() > 380:
        head.setx(-380)

    if head.xcor() < -380:
        head.setx(380)

    if head.ycor() > 280:
        head.sety(-280)

    if head.ycor() < -280:
        head.sety(280)

# Add to the snake when not touching food
def redraw_snake():
    slen = len(snake)

    if slen != 1 :
        if head.heading() == 90 :
            x = 0
            y = 0

        if head.heading() == 180 :
            x = 0
            y = 0

        if head.heading() == 270 :
            x = 0
            y = 0

        if head.heading() == 0 :
            x = 0
            y = 0



# Add to the snake when it eats the food
def addto_snake(newTail):
    slen = len(snake)
    lastTail = snake[slen-1]

    print (slen)  
    print (lastTail.heading())

    if lastTail.heading() == 90 :
        x = lastTail.xcor() - 20
        y = lastTail.ycor()

    if lastTail.heading() == 180 :
        x = lastTail.xcor()
        y = lastTail.ycor() + 20

    if lastTail.heading() == 270 :
        x = lastTail.xcor() + 20
        y = lastTail.ycor()

    if lastTail.heading() == 0 :
        x = lastTail.xcor()
        y = lastTail.ycor() - 20

    object_frame(tail)
    newTail.color("brown")
    newTail.goto(x, y)
    newTail._setmode(mode = "logo")
    snake.append(newTail)

# Main program starts from here
snake = []
winWidth = 800 
winHeight = 600

# turtle window
window = turtle.Screen()
window.title("Dinku Snake")
window.bgcolor("black")
window.setup(winWidth, winHeight)
window.tracer(0)

# Initializing the snake head
head = turtle.Turtle()
snake.append(new_snake(head))

slen = len(snake)

# Initializing the food
food = turtle.Turtle()
object_frame(food)
food.color("green")

# keyboard binding
window.listen()
window.onkeypress(move_left,"Left")
window.onkeypress(move_down,"Down")
window.onkeypress(move_right,"Right")
window.onkeypress(move_up,"Up")

show_food(food)

while True:
    window.update()

    snakeCor = [head.xcor(),head.ycor()]
    foodCor = [food.xcor(),food.ycor()]

    if snakeCor == foodCor:
        tail = turtle.Turtle()
        addto_snake(tail)
        show_food(food)

    redraw_snake()
    check_boundary()


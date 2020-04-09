# modules

import turtle
import random
import time

# turtle window

window = turtle.Screen()

window.title("snake xenzia")
window.bgcolor("black")
window.setup(width = 800 , height = 600)
window.tracer(0)

# initializing a bunch of stuff

steps_behind_snake = 0

tail_total_no = 0.00

tail_arr1 = []

# initializing score

pscore = 0

score = turtle.Turtle()
score.color("white")
score.penup()
score.goto(0, 260)
score.hideturtle()

# initializing all turtle object's attributes

def object_frame(obj):
    obj.speed(0)
    obj.shape("square")
    obj.shapesize(stretch_wid = 0.9523 , stretch_len = 0.9523)
    obj.color("pink")
    obj.penup()
    obj.goto(1000,1000)

# head

snake = turtle.Turtle()
object_frame(snake)
snake.color("white")
snake.goto(0,0)
snake._setmode(mode = "logo")

# food

food = turtle.Turtle()
object_frame(food)
food.color("green")
food.goto(100,20)

# tails created bfore use

no_of_tails = 100

for i in range(no_of_tails):
    tail_arr1.append(turtle.Turtle())

for tail in tail_arr1:
    object_frame(tail)

# infinite moves

direction = ""

def inf_right():
    x = snake.xcor()
    x += 20
    snake.setx(x)
    snake.seth(90)
    return True

def inf_left():
    x = snake.xcor()
    x -= 20
    snake.setx(x)
    snake.seth(270)
    return True

def inf_up():
    y = snake.ycor()
    y += 20
    snake.sety(y)
    snake.seth(0)
    return True

def inf_down():
    y = snake.ycor()
    y -= 20
    snake.sety(y)
    snake.seth(180)
    return True

# function to return position of tail with respect to head
# input - target tail no.
# output - target tail_no.'s co-ords

def tail_pos():

    prev_pos = 0

    if snake.heading() == 90 :
        prev_pos = [reference_co[0] - 20 , reference_co[1]]

    if snake.heading() == 180 :
        prev_pos = [reference_co[0] , reference_co[1] + 20]

    if snake.heading() == 270 :
        prev_pos = [reference_co[0] + 20 , reference_co[1]]

    if snake.heading() == 0 :
        prev_pos = [reference_co[0] , reference_co[1] - 20]

    return prev_pos
# if tail_total_no >= 1:
#     tail1.goto(tail_pos(1))

def tail_follow(target_tail,target_tail_no):
    if tail_total_no >= target_tail_no:
        target_tail.goto(tail_pos(target_tail_no))



# keyboard binding

window.listen()
window.onkeypress(inf_left,"Left")
window.onkeypress(inf_down,"Down")
window.onkeypress(inf_right,"Right")
window.onkeypress(inf_up,"Up")

# reference coordinates

# main game loop

while True:

    window.update()
    reference_co = [snake.xcor(),snake.ycor()]

    # food coordinates

    food_co = [food.xcor(),food.ycor()]

    # loops a hundred times (for 100 tails)

    for tail in tail_arr1:
        

        # every time head eats food, a)new tail added behind head b)food teleports


        # tail follows head

        if tail.pos() != (1000,1000):

    
            if snake.heading() == 90 :
                prev_pos = [reference_co[0] - 20 , reference_co[1]]

            if snake.heading() == 180 :
                prev_pos = [reference_co[0] , reference_co[1] + 20]

            if snake.heading() == 270 :
                prev_pos = [reference_co[0] + 20 , reference_co[1]]

            if snake.heading() == 0 :
                prev_pos = [reference_co[0] , reference_co[1] - 20]

            tail.goto(prev_pos)

            reference_co = prev_pos

        snake_co = (snake.xcor(),snake.ycor())

        if [snake.xcor(),snake.ycor()] == food_co:
    
            # new tail added behind head

            if snake.heading() == 90:
                tail_arr1[ int(tail_total_no / 100)].goto(reference_co[0] - 20 , reference_co[1])

            if snake.heading() == 180:      # up-down
                tail_arr1[ int(tail_total_no / 100)].goto(reference_co[0] , reference_co[1] + 20)

            if snake.heading() == 270:       # right-left
                tail_arr1[ int(tail_total_no / 100)].goto(reference_co[0] + 20 , reference_co[1])

            if snake.heading() == 0:        # down-up 
                tail_arr1[ int(tail_total_no / 100)].goto(reference_co[0] , reference_co[1] - 20)


            tail_total_no += 1

            #  food teleports randomly

            food_new_x = random.randrange(-380,400,20)
            food_new_y = random.randrange(-280,280,20)
            food.goto(food_new_x,food_new_y) 

        # if snake hits boundary, goes back to start

        if snake.xcor() > 390:
            for tail in tail_arr1:
                snake.setx(0)
                snake.sety(0)
                tail.goto(1000,1000)

        if snake.xcor() < -400:
            for tail in tail_arr1:
                snake.setx(0)
                snake.sety(0)
                tail.goto(1000,1000)

        if snake.ycor() > 290:
            for tail in tail_arr1:
                snake.setx(0)
                snake.sety(0)
                tail.goto(1000,1000)
                              
        if snake.ycor() < -290:
            for tail in tail_arr1:
                snake.setx(0)
                snake.sety(0)
                tail.goto(1000,1000)
 




'''reference_co = snake_co
prev_pos = ...
for tail in tail_arr:
    reference_co = prev_pos
    if heading...:
        tail.goto(prev_pos)'''
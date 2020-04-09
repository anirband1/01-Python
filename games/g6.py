# modules

import turtle
import random
import sys
import time

# IN TERMINAL

level = int(input("choose your level from 1-5:  "))

no_of_enemies = int(input("how many enemies do you think you can shoot? "))

if no_of_enemies > 20:                       
    print("\n\nreally ?... i dont think your mom would allow so much screen time, Brenner\n")
    time.sleep(3)
    print("maximum no. of ships the dark side can send is 20.")
    print("bye")
    time.sleep(2)
    sys.exit()

else:
    print("\n\nokay...go!")
    time.sleep(2)


# IN TURTLE

p_score = 0
no_enemy_gone = 0

win = turtle.Screen()
win.title("alien attack")
win.setup(width = 600,height = 700)
win.bgcolor("black")
win.tracer(0)

# text function

def text_frame(txt,x,y):
    txt.color("white")
    txt.penup()
    txt.goto(x,y)
    txt.hideturtle()

# game over sign

game_over = turtle.Turtle()
text_frame(game_over,0,0)

# score of player

score = turtle.Turtle()
text_frame(score,0,260)

# turtle object function

def object_frame(obj):
    obj.speed(0)
    obj.shape("square")
    obj.color("white")
    obj.penup()

# main spaceship

ship = turtle.Turtle()
object_frame(ship)
ship.shapesize(stretch_wid = 2, stretch_len = 3)
ship.goto(0,-310)

# bullet

bullet = turtle.Turtle()
object_frame(bullet)
bullet.color("yellow")
bullet.shapesize(stretch_wid = 2.5, stretch_len = 0.25)
bullet.dy = 30

# enemies

enemies = []
# has to be > 2

for i in range(no_of_enemies):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    object_frame(enemy)
    enemy.goto(random.randrange(-270,270,30),random.randrange(280,no_of_enemies * 110,30))
    enemy.dy = -level

# move function

def ship_right():
    x = ship.xcor() 
    x += 30
    ship.setx(x)

def ship_left():
    x = ship.xcor()
    x -= 30
    ship.setx(x)

def shoot():
    bullet.setx(ship.xcor())
    bullet.sety(ship.ycor())

# binding

win.listen()
win.onkeypress(ship_right, "Right")
win.onkeypress(ship_left, "Left")
win.onkeypress(shoot, "w")

#main loop

while True:
    win.update()
    for enemy in enemies:

        # playing with enemies which are not dead

        if enemy.isvisible():

            shot = False
            # bullet moving up

            bullet.sety(bullet.ycor() + bullet.dy)

            # enemies moving down

            enemy.sety(enemy.ycor() + enemy.dy)    

            # enemy gets destroyed , bullet within screen

            if enemy.xcor() == bullet.xcor() and bullet.ycor() < 330 and enemy.ycor() < 330:
                enemy.hideturtle()
                no_enemy_gone += 1
                shot = True

            # score increment if enemy is shot and above ship

            if shot and enemy.ycor() > ship.ycor():
                p_score += 1  
                score.clear()  
                score.write(f"Score: {p_score}", align = "center", font = ("Courier", 24 ))

            # to count enemies which avoid ship as gone but doesnt increment score

            if enemy.ycor() <= ship.ycor():
                no_enemy_gone += 1
                enemy.hideturtle()

            if ship.xcor() < -270:
                ship.setx(-270)

            if ship.xcor() > 270:
                ship.setx(270)


    if no_enemy_gone == no_of_enemies:
        game_over.write("GAME OVER", align = "center", font = ("Courier", 100 ))
        
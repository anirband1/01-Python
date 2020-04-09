import turtle

no_of_tails = 300

tail_arr1 = []
x=0
y=0


window = turtle.Screen()

window.title("snake xenzia")
window.bgcolor("black")
window.setup(width = 800 , height = 600)
window.tracer(0)

def object_frame(obj):
    obj.speed(0)
    obj.shape("square")
    obj.shapesize(stretch_wid = 0.9523 , stretch_len = 0.9523)
    obj.color("pink")
    obj.penup()
    obj.goto(1000,1000)




for i in range(no_of_tails):
    tail_arr1.append(turtle.Turtle())

for tail in tail_arr1:
    window.update()
    object_frame(tail)
    tail.goto(x,y)
    x+=1
    y+=1
print(len(tail_arr1))


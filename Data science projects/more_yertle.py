#VERY IMPORTANT NOTE: the snowflakes aare generated randomly. unfortunately, this means that there is a small chance
#that they can generate outside the snowglobe. if this happens, just re-run the project and hopefully you'll
#be luckier next time.


from turtle import Screen, Turtle
import random

COLOR = (.4, .4, 0.9)  # (154, 0, 254)
TARGET = (.8, .95, .95)  # (221, 122, 80)



screen = Screen()
screen.tracer(False)

WIDTH, HEIGHT = screen.window_width(), screen.window_height()

deltas = [(hue - COLOR[index]) / HEIGHT for index, hue in enumerate(TARGET)]

turtle = Turtle()
turtle.color(COLOR)

turtle.penup()
turtle.goto(-WIDTH/2, HEIGHT/2)
turtle.pendown()

direction = 1

for distance, y in enumerate(range(HEIGHT//2, -HEIGHT//2, -1)):

    turtle.forward(WIDTH * direction)
    turtle.color([COLOR[i] + delta * distance for i, delta in enumerate(deltas)])
    turtle.sety(y)

    direction *= -1

screen.tracer(True)


turtle.speed(100)
turtle.penup()
turtle.forward(WIDTH/2)
turtle.left(90)
turtle.forward(HEIGHT/2)
turtle.right(90)
turtle.pendown()
turtle.color("black")
turtle.circle(130)
turtle.penup()
turtle.right(190)
turtle.forward(40)
turtle.left(80)
turtle.pendown()
turtle.forward(80)
turtle.left(110)
turtle.forward(150)
turtle.left(110)
turtle.forward(86)
turtle.left(105)
turtle.penup()
turtle.forward(130)
turtle.write("this is a snowglobe", font=("arial", 15, "normal"))

turtle.teleport(20,0)
turtle.pendown()
turtle.color(0.59, 0.3, 0)
turtle.begin_fill()
turtle.right(125)
turtle.forward(100)
turtle.left(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(100)
turtle.end_fill()
turtle.penup()
turtle.right(180)
turtle.forward(120)
turtle.right(90)
turtle.forward(10)
turtle.color("green")
turtle.begin_fill()
turtle.right(60)
turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.end_fill()



for x in range(3):
    turtle.teleport((-60+50*x), (70+30*x))
    for i in range(10):
        turtle.pendown()
        turtle.color("white")
        turtle.begin_fill()
        turtle.circle(2)
        turtle.end_fill()
        turtle.penup()
        turtle.right(random.randint(10,170))
        turtle.forward(30)


turtle.penup()
turtle.teleport(-50, 300)
turtle.write("dear aiden, Hapy holidays. enjoy your snow globe. -oliver", font=("arial",12,"normal"))
turtle.teleport(10, 120)

turtle.color("yellow")
turtle.shape("triangle")
screen.exitonclick()

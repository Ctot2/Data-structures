import turtle

yertle = turtle.Turtle()
yertle.getscreen().setup(1000, 800)
yertle.speed(5)
yertle.shape("turtle")


from turtle import Screen, Turtle

COLOR = (1, 0, 0)  # (154, 0, 254)
TARGET = (0, 0, 0)  # (221, 122, 80)



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


yertle.penup()
yertle.left(90)
yertle.forward(HEIGHT/2)
yertle.right(180)
yertle.pendown()
yertle.color("red")
yertle.forward(HEIGHT)

# Colorful Triangle
print(HEIGHT)
yertle.right(180)
for i in range(8):
    yertle.color("red", "black")
    yertle.begin_fill()
    yertle.forward(100)
    yertle.right(120)
    yertle.forward(100)
    yertle.right(120)
    yertle.forward(100)
    yertle.right(120)
    yertle.forward(100)
    yertle.end_fill()
yertle.right(180)
for i in range(8):
    yertle.color("black", "red")
    yertle.begin_fill()
    yertle.forward(100)
    yertle.right(120)
    yertle.forward(100)
    yertle.right(120)
    yertle.forward(100)
    yertle.right(120)
    yertle.forward(100)
    yertle.end_fill()

screen.exitonclick()


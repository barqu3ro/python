import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.setup(600, 400)
screen.bgcolor("white")

# Create a turtle object
flag = turtle.Turtle()
flag.speed(2)

# Draw the red rectangle
flag.penup()
flag.goto(-200, 100)
flag.pendown()
flag.color("red")
flag.begin_fill()
for _ in range(2):
    flag.forward(400)
    flag.right(90)
    flag.forward(100)
    flag.right(90)
flag.end_fill()

# Draw the yellow stripes
flag.penup()
flag.goto(-200, 50)
flag.pendown()
flag.color("yellow")
flag.begin_fill()
for _ in range(2):
    flag.forward(400)
    flag.right(90)
    flag.forward(50)
    flag.right(90)
flag.end_fill()

# Hide the turtle
flag.hideturtle()

# Exit on click
turtle.done()

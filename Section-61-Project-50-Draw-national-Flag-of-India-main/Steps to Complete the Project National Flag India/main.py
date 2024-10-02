import turtle
from turtle import *

screen = turtle.Screen()

t = turtle.Turtle()
speed(0)

# initially penup()
t.penup()
t.goto(-400, 250)
t.pendown()

# TODO 1 Draw Orange Rectangle

t.color("orange")
t.begin_fill()
t.forward(800)
t.right(90)
t.forward(167)
t.right(90)
t.forward(800)
t.end_fill()
t.color("white")
t.left(90)
t.forward(167)

# TODO 2 Skip white area and draw Green rectangle
t.color("green")
t.begin_fill()
t.forward(167)
t.left(90)
t.forward(800)
t.left(90)
t.forward(167)
t.end_fill()

# TODO 3 Draw Blue Circle
t.penup()
t.goto(70, 0)
t.pendown()
t.color("navy")
t.begin_fill()
t.circle(70)
t.end_fill()


t.penup()
t.goto(60, 0)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(60)
t.end_fill()

# TODO 4 Draw Mini Blue Circles
t.penup()
t.goto(-57, -8)
t.pendown()
t.color("navy")
for i in range(24):
    t.begin_fill()
    t.circle(3)
    t.end_fill()
    t.penup()
    t.forward(15)
    t.right(15)
    t.pendown()

# TODO 5 Draw Small Blue Circle
t.penup()
t.goto(20, 0)
t.pendown()
t.begin_fill()
t.circle(20)
t.end_fill()
# TODO 6 Draw Spokes
t.penup()
t.goto(0, 0)
t.pendown()
t.pensize(2)
for i in range(24):
    t.forward(60)
    t.backward(60)
    t.left(15)

# to hold the
# output window
turtle.done()




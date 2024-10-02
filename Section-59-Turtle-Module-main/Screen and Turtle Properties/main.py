import turtle
from turtle import Turtle, Screen
import random


turtle.colormode(255)

screen = Screen()
new_turtle = Turtle()
new_turtle.penup()
new_turtle.goto(0, 200)
new_turtle.pendown()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_polygon(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        new_turtle.forward(100)
        new_turtle.right(angle)


new_turtle.color(random_color())
turtle.bgcolor(random_color())
# turtle.bgpic("python.gif")
turtle.title("Python for Everyone")
new_turtle.shapesize(10,5,1)
new_turtle.pensize(10)
new_turtle.speed(10)
draw_polygon(6)

new_turtle.clear()

screen.exitonclick()
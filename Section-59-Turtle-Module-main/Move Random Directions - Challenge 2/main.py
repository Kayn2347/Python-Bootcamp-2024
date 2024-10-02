import turtle as t
import random


t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


my_turtle = t.Turtle()
screen = t.Screen()
directions = [0, 90, 180, 270]
my_turtle.pensize(10)
my_turtle.speed(10)
for _ in range(250):
    my_turtle.color(random_color())
    my_turtle.forward(40)
    my_turtle.setheading(random.choice(directions))




screen.exitonclick()

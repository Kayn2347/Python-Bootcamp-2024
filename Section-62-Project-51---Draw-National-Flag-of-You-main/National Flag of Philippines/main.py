# Flag

import turtle as turtle

turtle.speed(20)
turtle.width(2)
turtle.Screen().bgcolor('gray')

def blue():
    # Blue Side
    turtle.penup()
    turtle.goto(140,180)
    turtle.pendown()
    turtle.color('blue')
    turtle.begin_fill()
    # Start
    turtle.goto(140, 80)
    turtle.goto(-140, 80)
    turtle.goto(-140, 180)
    turtle.goto(140,180)
    turtle.end_fill()
    return None

def red():
    # Red Side
    turtle.penup()
    turtle.goto(140, 80)
    turtle.pendown()
    turtle.color('red')
    turtle.begin_fill()
    # Start
    turtle.goto(-140, 80)
    turtle.goto(-140, -20)
    turtle.goto(140, -20)
    turtle.goto(140, 80)
    turtle.end_fill()
    return None

def triangle():
    # White Side
    turtle.color('white')
    turtle.begin_fill()
    turtle.goto(140, -20)
    turtle.goto(140, 180)
    turtle.goto(50, 80)
    turtle.goto(140, -20)
    turtle.end_fill()
    return None

def star():
    # Star 1
    turtle.penup()
    turtle.goto(125, 160)
    turtle.pendown()
    turtle.color('yellow')
    turtle.begin_fill()
    turtle.width(1)
    for i in range(5):
        turtle.forward(10)
        turtle.right(144)
    turtle.end_fill()
    
    # Star 2
    turtle.penup()
    turtle.goto(125, 0)
    turtle.pendown()
    turtle.color('yellow')
    turtle.begin_fill()
    turtle.width(1)
    for i in range(5):
        turtle.forward(10)
        turtle.right(144)
    turtle.end_fill()
    
    # Star 3
    turtle.penup()
    turtle.goto(60, 80)
    turtle.pendown()
    turtle.color('yellow')
    turtle.begin_fill()
    turtle.width(1)
    for i in range(5):
        turtle.forward(10)
        turtle.right(144)
    turtle.end_fill()
    return None

def drawFourRays(t, length, radius):
    turtle.width(4)
    for i in range(4):
        t.penup()
        t.forward(radius)
        t.pendown()
        t.forward(length)
        t.penup()
        t.backward(length + radius)
        t.left(90)
    turtle.width(2)
        
def sun():
    # Sun 
    turtle.penup()
    turtle.goto(115, 70)
    turtle.pendown()
    turtle.color('yellow')
    turtle.begin_fill()
    turtle.pendown()
    turtle.circle(10)
    
    turtle.goto(115, 80)
    turtle.pendown()
    drawFourRays(turtle, 10, 10)
    turtle.right(45)
    drawFourRays(turtle, 10, 10)
    turtle.left(45)
    
    turtle.end_fill()
    return None

blue()
red()
triangle()
star()
sun()

turtle.end_fill()
turtle.done()


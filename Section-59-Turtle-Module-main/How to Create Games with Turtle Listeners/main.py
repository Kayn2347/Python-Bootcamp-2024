from turtle import Turtle, Screen


my_turtle = Turtle()
screen = Screen()
my_turtle.pensize(4)


def up():
    my_turtle.setheading(90)
    my_turtle.forward(40)


def down():
    my_turtle.setheading(270)
    my_turtle.forward(40)


def left():
    my_turtle.setheading(180)
    my_turtle.forward(40)


def right():
    my_turtle.setheading(0)
    my_turtle.forward(40)


def red():
    my_turtle.color("red")


def green():
    my_turtle.color("green")


def blue():
    my_turtle.color("blue")


def black():
    my_turtle.color("black")


screen.listen()
screen.onkey(fun=up, key="Up")
screen.onkey(fun=down, key="Down")
screen.onkey(fun=left, key="Left")
screen.onkey(fun=right, key="Right")
screen.onkey(fun=red, key="r")
screen.onkey(fun=green, key="g")
screen.onkey(fun=blue, key="b")
screen.onkey(fun=black, key="x")



screen.exitonclick()
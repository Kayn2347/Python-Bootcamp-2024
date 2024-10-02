from turtle import Turtle, Screen


new_turtle = Turtle()
screen = Screen()


for _ in range(4):
    new_turtle.forward(150)
    new_turtle.right(90)

screen.exitonclick()
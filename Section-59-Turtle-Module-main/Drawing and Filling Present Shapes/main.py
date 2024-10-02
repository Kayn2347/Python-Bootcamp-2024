# Drawing Present Shapes
from turtle import Turtle, Screen


new_turtle = Turtle()
screen = Screen()

new_turtle.begin_fill()
new_turtle.fillcolor("green")
new_turtle.pensize(10)
new_turtle.circle(100)
new_turtle.end_fill()
new_turtle.hideturtle()

screen.exitonclick()

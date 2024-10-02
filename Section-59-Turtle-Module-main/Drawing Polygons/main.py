from turtle import Turtle, Screen


screen = Screen()
new_turtle = Turtle()
new_turtle.penup()
new_turtle.goto(0, 200)
new_turtle.pendown()


def draw_polygon(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        new_turtle.forward(150)
        new_turtle.right(angle)


draw_polygon(10)
screen.exitonclick()
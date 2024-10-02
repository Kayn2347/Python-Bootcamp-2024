from turtle import Screen, Turtle
import random


screen = Screen()
screen.setup(width=900, height=400)
user_option = screen.textinput(title="Choose Turtle Color", prompt="Choose color: (red, silver, gold, green, blue, "
                                                                   "black) ")

colors = ["red", "silver", "gold", "green", "black"]
y_position = -100
all_turtles = []
# Create 6 turtles and change y position to locate turtles next to each other at start line
for turtle_color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.shapesize(2)
    new_turtle.fillcolor(turtle_color)
    new_turtle.goto(x=-430, y=y_position)
    y_position += 50
    all_turtles.append(new_turtle)

# for message
output_turtle = Turtle()
output_turtle.hideturtle()
output_turtle.penup()
output_turtle.goto(-200,0)

race_is_on = False
if user_option:
    race_is_on = True

while race_is_on:
    for turtle in all_turtles:
        if turtle.xcor() > 420:
            race_is_on = False
            winning_color = turtle.fillcolor()
            if winning_color == user_option:
                message = f"You have won!!! The winner is {winning_color} turtle!"
                output_turtle.write(message, font=('Arial', 26, 'normal'))
            else:
                message = f"You have lost!!! The winner is {winning_color} turtle!"
                output_turtle.write(message, font=('Arial', 26, 'normal'))
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)



screen.exitonclick()
# Import Turtle Module
import turtle


# Create Turtle Object
new_turtle = turtle.Turtle()
screen = turtle.Screen()


# Create a function to draw a circle with dynamic radius and color.
def draw_circle(col, rad):
    # Set the fill
    new_turtle.fillcolor(col)
    # Start filling the color
    new_turtle.begin_fill()
    # Draw a circle
    new_turtle.circle(rad)
    # Ending the filling of the color
    new_turtle.end_fill()


# Draw ears of Panda with black color circles.
# First ear
new_turtle.up()
new_turtle.setpos(-35, 95)
new_turtle.down
draw_circle('black', 15)

# Second ear
new_turtle.up()
new_turtle.setpos(35, 95)
new_turtle.down()
draw_circle('black', 15)

# Draw face of Panda with white color circle.
new_turtle.up()
new_turtle.setpos(0, 35)
new_turtle.down()
draw_circle('white', 40)

# Draw eyes of Panda with black and white color concentric circles.

# First eye
new_turtle.up()
new_turtle.setpos(-18, 75)
new_turtle.down
draw_circle('black', 8)

# Second eye
new_turtle.up()
new_turtle.setpos(18, 75)
new_turtle.down()
draw_circle('black', 8)

# Draw eyes white

# First eye
new_turtle.up()
new_turtle.setpos(-18, 77)
new_turtle.down()
draw_circle('white', 4)

# Second eye
new_turtle.up()
new_turtle.setpos(18, 77)
new_turtle.down()
draw_circle('white', 4)

# Draw nose of Panda with black color circle.
new_turtle.up()
new_turtle.setpos(0, 55)
new_turtle.down
draw_circle('black', 5)

# Draw two semicircle for mouth below nose.
new_turtle.up()
new_turtle.setpos(0, 55)
new_turtle.down()
new_turtle.right(90)
new_turtle.circle(5, 180)
new_turtle.up()
new_turtle.setpos(0, 55)
new_turtle.down()
new_turtle.left(360)
new_turtle.circle(5, -180)
new_turtle.hideturtle()

screen.exitonclick()



import turtle
import pandas

screen = turtle.Screen()
screen.title("Schengen Countries Game")
image = "map.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("countries.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 26:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/26 Countries Correct",
                                    prompt="What's another country's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("countries_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state, font=('Arial', 14))

# To get the x and y coordinates
# def buttonclick(x, y):
#     print("You clicked at this coordinate({0},{1})".format(x, y))
#
#
# # onscreen function to send coordinate
# turtle.onscreenclick(buttonclick, 1)
# turtle.listen()  # listen to incoming connections
# turtle.speed(10)  # set the speed




# turtle.done()
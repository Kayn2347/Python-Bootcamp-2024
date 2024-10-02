from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("red")
        self.penup()
        self.shapesize(stretch_wid=0.6, stretch_len=0.6)
        self.speed("fastest")
        self.move_new_location()

    def move_new_location(self):
        rand_x = random.randint(-300, 300)
        rand_y = random.randint(-300, 300)
        self.goto(rand_x, rand_y)


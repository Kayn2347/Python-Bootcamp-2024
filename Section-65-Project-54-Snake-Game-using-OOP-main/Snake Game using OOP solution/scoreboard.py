from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0,300)
        self.hideturtle()
        self.score_update()

    def score_update(self):
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, 'normal'))

    def update_score(self):
        self.score += 1
        self.clear()
        self.score_update()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Courier", 24, 'normal'))
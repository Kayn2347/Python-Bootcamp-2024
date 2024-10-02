from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


game_screen = Screen()
game_screen.setup(width=650, height=650)
game_screen.bgcolor("gray")
game_screen.title("Snake Game")
game_screen.tracer(0)

snake = Snake()
food = Food()
board = Scoreboard()

game_screen.listen()
game_screen.onkey(snake.up, 'Up')
game_screen.onkey(snake.down, 'Down')
game_screen.onkey(snake.left, 'Left')
game_screen.onkey(snake.right, 'Right')

game_on = True
while game_on:
    game_screen.update()
    time.sleep(0.3)
    snake.move()
    #  Detect collision with food
    if snake.snake_head.distance(food) < 20:
        print("test")
        food.move_new_location()
        snake.extend_snake()
        board.update_score()


    # Detect collision with wall
    if snake.snake_head.xcor() > 300 or snake.snake_head.xcor() < -300 or snake.snake_head.ycor() > 300 or snake.snake_head.ycor() < -300:
        game_on = False
        board.game_over()

    # Detect collision with Tail
    for part in snake.snake_parts[1:]:
        if snake.snake_head.distance(part) < 15:
            game_on = False
            board.game_over()




game_screen.exitonclick()
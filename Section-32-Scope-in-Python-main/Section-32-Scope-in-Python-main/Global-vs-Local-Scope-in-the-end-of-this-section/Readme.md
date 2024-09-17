score = 0 

# def increase_score():
#     score = 1
#     print(f"Score inside function: {score}")

# increase_score()
# print(f"Score outside function: {score}")

# Local scope
# def change_color():
#     color = "Red"
#     print(color)

# change_color()
# print(color)


# Global Scope
player_score = 0

def game():
  def change_color():
     color = "Red"
     print(player_score)
  change_color()

game()
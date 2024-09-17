clubs = (("FC Barcelona", "Spain", 1899,
  [
      (3, "Pique"),
      (5, "Busquets"),
      (7, "Dembele"),
  ]
),
("Real Madrid CF", "Spain", 1902,
  [
      (7, "Hazard"),
      (9, "Benzema"),
      (10, "Modric"),
  ]
),
("Manchester United FC", "England", 1878,
  [
      (6, "Pogba"),
      (7, "Ronaldo"),
      (14, "Lingard"),
  ]
),
("Arsenal FC", "England", 1886,
  [
      (7, "Lacazette"),
      (14, "Aubameyang"),
      (16, "Holding"),
  ]
),
)


team = clubs[1]
country = team[1]
players = team[3]
player_details = players[2]
player_name = player_details[1]
# print(team)
# print(players)
# print(player_details)
# print(player_name)

# print(clubs[0] [03])
player_list = clubs [0] [3]
player =player_list.pop(0)
clubs[2] [3].append(player)
print(clubs[0])
print(clubs[2])

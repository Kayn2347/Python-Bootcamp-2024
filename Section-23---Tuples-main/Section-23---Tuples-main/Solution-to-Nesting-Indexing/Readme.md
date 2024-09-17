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


# The name of first player from Arsenal
# The year that Manchester United FC founded.
# Squad number of Dembele
# The tuple representing the 2nd player in Real Madrid CF
print(clubs[3][3][0][1])
print(clubs[2][2])
print(clubs[0][3][2][0])
print(clubs[1][3][1])


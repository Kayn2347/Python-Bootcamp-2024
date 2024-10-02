class StarCookie:
    milk = 0.1

def __init__(self, color, weight):
        self.color = color 
        self.weight = weight


star_cookie1 = StarCookie("red", 16)
star_cookie2 = StarCookie("blue", 15)
StarCookie.milk = 0.2

print(star_cookie1.__dict__)
print(star_cookie2.__dict__)
print(StarCookie.__dict__)
print(star_cookie1.milk)
print(star_cookie2.milk)
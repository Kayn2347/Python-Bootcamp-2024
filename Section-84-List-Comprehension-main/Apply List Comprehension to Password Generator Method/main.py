


def generate_password():
    password = ""
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFIGHIJKLMNOPQRSTUVWXYZ"
    nums = "1234567890"
    symbols = "-+=!@#$%^&*"
    for char in range(1, randint(8, 12)):
        password += choice(letters)
    for num in range(1, randint(3, 5)):
        password += choice(password)
    for sysbol in range(1, randint(3, 5)):
        password+= choice(symbols)
    password_list = list(password)
    shuffle(password_list)
    password = "".join(password_list)
    return password


def generate_password_lc():
  letters = "abcdefghijklmnopqrstuvwxyzABCDEFIGHIJKLMNOPQRSTUVWXYZ"
  nums = "1234567890"
  symbols = "-+=!@#$%^&*"
  password_letters =[choice(letters) for i in range(1,randint(8, 12)]
  password_numbers =[choice(num) for _ in range(1,randint(3, 5))]
  password_symbols =[choice(symbol) for _ in range(1,randint(3, 5))]
  password_list = password_letters + password_numbers + password_sysmbols
  shuffle(password_list)
  password = "".join(password_list)
  return password

generate_password_lc())

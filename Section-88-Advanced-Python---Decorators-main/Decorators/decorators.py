def do_twice(func):
    def wrapper():
        print("The function will be called twice.")
        func()
        func()
    return wrapper
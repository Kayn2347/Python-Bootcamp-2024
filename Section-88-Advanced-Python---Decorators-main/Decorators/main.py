import random


def my_decorator(func):
    def wrapper():
        print("Code execution before func call...")
        if random.randint(1, 20) > 10:
            func()
        print("Code execution after func call...")
    return wrapper


from decorators import do_twice


@do_twice
def say_hey():
    print("Heyyy!")


@do_twice
def say_hi():
    print("Hi!")


say_hey()
say_hi()
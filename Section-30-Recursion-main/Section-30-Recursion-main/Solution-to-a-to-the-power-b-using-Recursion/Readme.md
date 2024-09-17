def power(a,b):
    if b < 0 or not isinstance(a, int) or not isinstance(b, int):
        return "not applicable"
    elif b == 0:
        return 1
    elif a == 0:
        return 0
    elif b == 1:
        return a
    else:
        return a*power(a,b-1)


print(power("a",-2))
def sum_positive(n):
    if not isinstance(n, int):
        return -1
    elif n < 1:
        return 0
    else:
        result = n + sum_positive(n - 2)
        return result

print(sum_positive(100))
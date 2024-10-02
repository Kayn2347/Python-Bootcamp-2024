import time
def is_divided(num):
    if num % 555 == 0:
        return True
    return False


def infinite_division():
    num = 0
    while True:
        if is_divided(num):
            i = (yield num)
            if i is not None:
                num = i
        num += 1


gen_obj = infinite_division()
for i in gen_obj:
    print(i)
    time.sleep(1)
    digits = len(str(i))
    if digits > 8:
        gen_obj.close()
    gen_obj.send(10**(digits))


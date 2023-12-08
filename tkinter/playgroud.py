def add(*args):
    sum = 0
    for i in args:
        sum += i

    return sum


def calculate(**kawargs):
    print(type(kawargs))
    for key, value in kawargs.items():
        print(key, value)


print(add(2, 3, 4, 545454))
calculate(add=5, wal=5645)

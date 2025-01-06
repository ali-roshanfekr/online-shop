import random


def creat_random_code(size: int):
    var = ""
    for item in range(0, size):
        var += str(random.choice(range(0, 10)))

    return var

# Random list and the last and first elements from list
import random


def func(c):
    b = [c[0], c[-1]]
    return b


def rand_list(d):
    while len(d) < 10:
        a = random.randint(1, 100)
        d.append(a)
    return d

d = []
print(rand_list(d))
print(func(rand_list(d)))
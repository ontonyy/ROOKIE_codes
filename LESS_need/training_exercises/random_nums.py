import random

class Dice:
    def roll(self):
        tup = (random.randint(1, 10), random.randint(1, 10))
        return tup

if __name__ == '__main__':
    print(Dice().roll())
import random

try:
    num = int(input("Age: "))
    y = str(input("Name: "))
    z = "Your quantity of chromosomes:"
    f = random.randrange(1, 100)
    print(z, f, "\nThis is so much,", y)
except:
    print("! Invalid input !")

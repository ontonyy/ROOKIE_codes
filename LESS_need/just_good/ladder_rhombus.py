name = str(input("Type some sign and make ladder: "))


def func(name1, x=1, y=8):
    while x < 9 and y > 0:
        print((x * str(name1) + (y * ' ' * 2) + x * str(name1)) + (x * ' ' + (y * str(name1) * 2) + x * ' '))
        x += 1
        y -= 1
    print("\nYou ladder is superb!\n")


def new(name2, y=8, x=1):
    while y > 0 and x < 9:
        print((y * str(name2)) + (x * ' ' * 2) + (y * str(name2)) + (y * ' ' + (x * str(name2) * 2) + y * ' '))
        y -= 1
        x += 1


new(name)
func(name)

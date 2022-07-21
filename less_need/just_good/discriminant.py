import math


def main():
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    D = math.pow(b, 2) - 4 * a * c
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        print("x1 = {:.2f} | x2 = {:.2f}".format(x1, x2))
    elif D < 0:
        return
    else:
        x = (-b + math.sqrt(D)) / (2 * a)
        print(abs(x))


if __name__ == '__main__':
    main()

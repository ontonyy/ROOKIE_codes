def summir(x):
    if len(x) == 0:
        return 0
    elif len(x) == 1:
        return x[0]
    else:
        return x[0] + summir(x[1:])

x = [5, 3, 4]
if __name__ == '__main__':
    print(summir(x))
def even_num(a, new_a):
    for x in a:
        if x % 2 == 0:
            new_a.append(x)
    print(new_a)

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
new_a = []

if __name__ == '__main__':
    even_num(a, new_a)
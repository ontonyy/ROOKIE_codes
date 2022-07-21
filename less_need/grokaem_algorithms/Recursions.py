def numbers(i):
    if i == 0:
        return i
    else:
        print(i)
        numbers(i - 1)

numbers(10)

def sum(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return i + sum(i-1)

if __name__ == '__main__':
    print(sum(10))


def multiply(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return i * multiply(i-1)

if __name__ == '__main__':
    print(multiply(5))

def fibo(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibo(x - 1) + fibo(x - 2)

for n in range(11):
    print(n, ":", fibo(n))


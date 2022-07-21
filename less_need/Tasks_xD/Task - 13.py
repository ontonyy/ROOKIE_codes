def Fibonacci(ans):
    if ans == 0:
        return 0
    elif ans == 1:
        return 1
    else:
        return Fibonacci(ans - 1) + Fibonacci(ans - 2)

ans = int(input("How many Fibonacci numbers do you want: "))
if __name__ == '__main__':
    Fibonacci(ans)
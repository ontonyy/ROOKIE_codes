n = int(input("Whole number: "))
fizz = 'Fizz'
bizz = 'Bizz'
for x in range(1, n):
    if x % 3 == 0 and x % 5 == 0:
        print("    FIZZbizz    ")
        continue
    elif x % 2 == 0:
        for y in fizz:
            print(y)
        continue
    elif x % 3 == 0:
        for y in bizz:
            print("           ", y)
        continue
    print("---------->", x)

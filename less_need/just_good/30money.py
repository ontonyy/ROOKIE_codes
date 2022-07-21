
n = 0
day = 0
while n < 30:
    n += 1
    cent = float(0.01 * (2 ** n))
    day += 1
    print(str(day) + " day: " + str(cent))

    if n == 30:
        print("Here is end!")
        exit()
        

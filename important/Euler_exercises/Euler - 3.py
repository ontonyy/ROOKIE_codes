import time
user_input = int(input("Number, which you want to control: "))
dec = []

for x in range(1, user_input):
    x += 1
    for i in range(2, x):
        if (x % i) == 0:
            break
        else:
            dec.append(x)
            break

for y in dec:
    if user_input % y == 0:
        start_time = time.time()
        print("The took {} seconds.\n".format(time.time()-start_time))
        print("The higher divisor {}".format(y))


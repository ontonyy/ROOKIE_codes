dec = str(input("What kind of action you need(+, -, *, /): "))
if dec != "+" and dec != "-" and dec != "*" and dec != "/":
    print("Try again!")
    exit()


def calc():
    x = int(input("First: "))
    y = int(input("Second: "))
    z = int(input("Third: "))
    if dec == "+":
        print("Yours answer is ", x + y + z)
    if dec == "-":
        print("Yours answer is ", x - y - z)
    if dec == "*":
        print("Yours answer is ", x * y * z)
    if dec == "/":
        print("Yours answer is ", x / y / z)


while not dec:
    print("Try again!")

calc()
input("Press enter to exit...")

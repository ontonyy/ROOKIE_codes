numbers = [5, 3, 4, 9, 11, 5, 6, 3]

for x in numbers:
    print(x * "x")


max = numbers[0]

for x in numbers:
    if x > max:
        max = x

print(max)

uniques = []
for x in numbers:
    if x not in uniques:
        uniques.append(x)

print(uniques)
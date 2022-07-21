num = [1, 2]
total = 0

for i in range(4000000):
    if i == num[-1] + num[-2]:
        num.append(i)

for n in num:
    if n % 2 == 0:
        total += n

print('Вот так то это решается блин блин\nСумма получилась:', total)
print(num)
print(total)

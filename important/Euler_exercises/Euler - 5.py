list = []
answer = 1

for i in range(1, 11):
    list.append(i)

for i in range(1, 10):
    for j in range(1, i+1):
        if list[i] % list[i-j] == 0:
            list[i] = int(list[i] / list[i-j])


for i in range(0, len(list)):
    answer = answer * list[i]

print(answer)
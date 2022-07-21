# Triangle numbers
num_list = list(range(1, 100000))
add_list = []
x = 1
while len(add_list) < 100000:
    # 1 + 2 + 3 ... + 8 ...
    add_list.append(sum(num_list[:x]))
    x += 1

divide_list = []
max_nums = []

for num in add_list:
    for x in range(1, 100000):
        if num % x == 0:
            divide_list.append(x)
    if len(divide_list) > 500:
        max_nums.append(num)
        print(f"{num} : {''.join(str(divide_list))}")
        print(len(divide_list))
        break
    else:
        divide_list.clear()

print(max_nums)

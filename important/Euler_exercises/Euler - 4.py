import heapq

nums = []

for x in range(100, 1000):
    for y in range(100, 1000):
        z = x * y
        zs = str(z)
        if zs == zs[::-1]:
            print(z)
            nums.append(z)
            break

greatest_num = str(heapq.nlargest(1, nums))
print("The greatest palindrome is - " + greatest_num)


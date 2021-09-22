import time

divisors = []
nums = []
start = time.time()

for x in range(2, 150000):
    for y in range(2, 150000):
        if x % y == 0:
            print(f'{x} : {y}')
            divisors.append(y)
    if len(divisors) <= 1:
        nums.append(x)
        divisors.clear()
    elif len(divisors) > 1:
        divisors.clear()
print(nums)
print(len(nums), '<-- all nums')
print(nums[10000])

end = time.time()

print(f"Taked time {end - start}")
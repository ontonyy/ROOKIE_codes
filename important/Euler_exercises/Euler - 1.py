num_sum = []
num = int(input('How many numbers: '))
for n in range(num):
    if n % 3 == 0 or n % 5 == 0:
        print(n)
        num_sum.append(n)
print("Sum of elements in given list is :", sum(num_sum))
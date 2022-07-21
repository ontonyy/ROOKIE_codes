squared = []
sum_squared = []

for x in range(1, 101):
    y = x ** 2
    squared.append(y)

x = range(1, 101)
sum_squared.append(pow(sum(x), 2))

s_squared = sum(squared)
s_sum_squared = sum(sum_squared)

print(s_squared, "<--- every num in square(first 10 nums)")
print(s_sum_squared, "<--- first 10 nums summa and after, whole num square\n")
print(s_sum_squared - s_squared)

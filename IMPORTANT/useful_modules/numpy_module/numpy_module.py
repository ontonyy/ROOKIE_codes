import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# print(arr.reshape(-1))

for x in arr:
    for y in x:
        print(y)

print(np.array_split(arr, 4))
print(np.searchsorted(arr, 7))

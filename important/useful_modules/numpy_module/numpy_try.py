import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(0, 100, 111)

x2 = np.array([-0.5, 1, 3.5])
bins = np.array([0, 1, 2, 3])

print(np.digitize(x2, bins))

print(np.random.randint(1, 10, 10))
print(np.random.choice(["cristall", "sosun", "mishka", "corabl"], 5))

x3 = np.array([[1, 2, 3], [2, 4, 3], [5, 7, 9], [10, 8, 6]])

print(np.argmax(x3, 1))  # return max values from each list

x4 = np.array([5, 15, 20, 35, 50])
print(x4.mean())

print(np.eye(5))

x5 = np.arange(4)
print(x5)
print(x5.reshape(2, 2))

x6 = np.arange(5)
y6 = np.arange(5, 10)

print(f"X: {x6}, Y: {y6}\nSum: {np.add(x6, y6)}, Subtract: {np.subtract(x6, y6)}\nMultiply: {np.multiply(x6, y6)}, Divide: {np.divide(x6, y6)}")

x7 = np.genfromtxt("file.csv", dtype=None, encoding=None, delimiter=",") # read info from file
print(x7)





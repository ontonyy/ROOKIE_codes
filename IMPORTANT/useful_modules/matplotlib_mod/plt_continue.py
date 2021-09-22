import matplotlib.pyplot as plt
import numpy as np

# plot 1
x = np.array([0, 4, 8])
y = np.array([0, 20, 10])

plt.subplot(2, 3, 1)
plt.plot(x, y)
plt.title('FIRST')

# plot2

x1 = np.array([0, 2, 6])
y1 = np.array([15, 5, 25])

plt.subplot(2, 3, 2)
plt.plot(x1, y1)
plt.title('SECOND')

x2 = np.array([0, 4, 8])
y2 = np.array([0, 20, 10])

plt.subplot(2, 3, 3)
plt.plot(x2, y2)
plt.title('FIRST')

# plot2

x3 = np.array([0, 2, 6])
y3 = np.array([15, 5, 25])

plt.subplot(2, 3, 4)
plt.plot(x3, y3)
plt.title('SECOND')

x4 = np.array([0, 4, 8])
y4 = np.array([0, 20, 10])

plt.subplot(2, 3, 5)
plt.plot(x4, y4)
plt.title('FIRST')

# plot2

x5 = np.array([0, 2, 6])
y5 = np.array([15, 5, 25])

plt.subplot(2, 3, 6)
plt.plot(x5, y5)
plt.title('SECOND')
plt.show()


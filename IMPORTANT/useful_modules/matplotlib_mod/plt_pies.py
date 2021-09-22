import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
myLabels = ["Bananas", "Apples", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]


plt.pie(y, labels=myLabels, explode=myexplode)
plt.legend(title = 'Fruits: ')
plt.show()
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

values = [15, 15, 15, 15, 15, 15, 15]
plt.hist(values, 7, histtype='bar', align='mid', color='c', label='Test score Data', edgecolor='black')
plt.legend()
plt.title('Histogram of score')
plt.show()


def some_function():
    return 2

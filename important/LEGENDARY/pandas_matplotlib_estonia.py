import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import requests

pop = pd.read_csv('C:\main_modules\projects\special_files\ee (1).csv')
xl = pd.read_excel('C:\main_modules\projects\special_files\ee.xlsx')



print(pop.head().loc[:, ['city', 'population']])
plt.plot(pop.head().city, pop.head().population, marker='o')

plt.legend()
plt.show()
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


player = pd.read_excel(
    'C:\main_modules\projects\special_files/fifa_players.xlsx')

player.dropna(subset=['Club'], inplace=True)
barcelona = player.loc[player.Club == 'FC Barcelona', ['Club', 'Name', 'Rating', 'Nation']]
print(barcelona)

print('\nAbove only FC Barcelona Players\n\nHere is players with more than 30 years old\n')

print(player.loc[player['Age'] > 30, ['Name', 'Age', 'Rating']])

age1 = player.loc[player['Age'] > 30].count()[0]
age2 = player.loc[player['Age'] < 30].count()[0]

plt.pie([age1, age2], labels=['Ages > 30', 'Ages < 30'], colors=['cyan', 'blue'], autopct='%.2f %%')
plt.title('Fifa players AGES')
plt.show()

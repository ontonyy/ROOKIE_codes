import json
import pandas as pd
import matplotlib.pyplot as plt

main_string = ""
with open("main_all.json", "r") as file:
    for line in file.readlines():
        main_string += line

main_dict = json.loads(main_string)
df = pd.DataFrame(main_dict['213088'])
print(df)

df.plot(x='month', y='amount_total')
plt.show()

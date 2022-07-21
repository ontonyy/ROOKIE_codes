import pandas as pd
import matplotlib as plt

myvar = pd.DataFrame({
    'country': ['USA', 'Russia', 'Estonia'],
    'population': [10000, 5000, 1000],
    'year': [1990, 2000, 2010]
})
print(myvar)
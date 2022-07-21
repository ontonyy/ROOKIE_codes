import pandas as pd

data = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2],
    'countries': ['Germany', 'Sweden', 'USA']
}
myvar = pd.DataFrame(data, index=['x', 'y', 'z'])

print(myvar, '\n')


days = {
    'day1': 320,
    'day2': 380,
    'day3': 300
}
mydays = pd.Series(days)
print(mydays)
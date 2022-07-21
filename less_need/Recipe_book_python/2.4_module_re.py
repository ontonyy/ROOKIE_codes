import re
datepat = re.compile(r'\d+/\d+/\d+')
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
d = datepat.findall(text)
print(d)

for month, year, day in datepat.findall(text):
    print(f"{year} / {month} / {day}")
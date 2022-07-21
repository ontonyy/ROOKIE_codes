import re

text = 'UPPER PYTHON, lower python, Mixed Python'
r = re.findall('python', text, flags=re.IGNORECASE)
print(r)
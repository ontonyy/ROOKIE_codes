# Web site information checking

# Чтение заголовков с помощью двух способов

import requests
from bs4 import BeautifulSoup

# Первый способ

# r = requests.get('https://rus.err.ee/')
# soup = BeautifulSoup(r.text, features="lxml")
#
# for header in soup.find_all(class_="header-font two-font"):
#     if header.a:
#         print("\n", header.a.text)
#     else:
#         print(header.contents[0])
#

# Второй способ

url = 'https://rus.err.ee/'
r = requests.get(url)
ttl_lst = []


soup = BeautifulSoup(r.text, features="lxml")
title = soup.findAll('h2', {'class': 'header-font two-font'})

for row in title:
    ttl_lst.append(row.text)

print("\n\n ".join(ttl_lst))
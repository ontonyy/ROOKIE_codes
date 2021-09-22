import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.pravda.com.ua/rus/news/2021/06/13/7297055/')
soup = BeautifulSoup(r.text, 'lxml')
info = soup.find('div', class_='post_text')
matches = info.find_all('p')

data = []
del matches[:5]
for match in matches[::-1]:
    data.append(match.text)


print('\n\n'.join(data))
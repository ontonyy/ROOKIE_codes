import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.euro-football.ru/category/result/1003096931')

soup = BeautifulSoup(r.text, "lxml")

score = soup.find_all('div', class_='calendar-item__match')     # Счёт матча
times = soup.find_all('div', class_='calendar-item__time')      # Время матча
calendar = soup.find_all('div', class_='calendar__list')    # Полная информация о матче
days = soup.find_all('span', class_='calendar-list__day')


# matches = []
# for c in calendar[:]:
#     matches.append(c.text.strip())
#
# print(''.join(matches))


scores = []
daiz = []
timez = []
for s in score:
    scores.append(s.text.strip('\n\n'))

for day in days:
    daiz.append(day.text)

for time in times:
    timez.append(time.text)

# Принтует просто время матча
# for x, time in zip(scores, times):
#     print(f'\n--> {time.text} <--\n\n' + x.strip('\n'))


# Принтует матчи за 13 июня
for x, y in zip(scores[:3], timez[:3]):
    print('\nDAY MATCH --> ' + daiz[0] + " || " + y + '\n\n' + x)

# Принтует матчи за 12 июня
for x, y in zip(scores[3:6], timez[3:6]):
    print('\nDAY MATCH --> ' + daiz[1] + " || " + y + '\n\n' + x)




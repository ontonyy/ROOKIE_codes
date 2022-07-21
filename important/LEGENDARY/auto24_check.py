import requests
from bs4 import BeautifulSoup
from math import ceil
import csv
import xlsxwriter
import os

URL = "https://rus.auto24.ee/kasutatud/nimekiri.php?bn=2&a=101102&ssid=14472913&b=44&ae=2&af=50&by=2&otsi=%D0%BF%D0%BE%D0%B8%D1%81%D0%BA&ak=50"

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
           'accept': '*/*'}

FILE = input('File name: ') + '.xlsx'


def get_link(url, params=None):
    r = requests.get(url, params=params, headers=HEADERS)
    return r


def get_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    all_cars = soup.find('div', class_='current-range')
    car_nums = all_cars.find('strong')
    return car_nums.string


def get_content(html):
    soup = BeautifulSoup(html, 'lxml')

    items = soup.find_all('a', class_='main')
    links = soup.find_all('a', class_='row-link')
    prices = soup.find_all('div', class_='finance')
    lisa = soup.find_all('div', class_='extra')

    new = []
    for item, link, price, l in zip(items, links, prices, lisa):
        i = item.find_all('span')

        try:
            car = f'{i[0].text} {i[1].text} | engine - {i[3].text}'
        except IndexError:
            continue

        print(car)
        p = price.find('span', class_='price').text
        new.append({
            'model': car,
            'price': p.replace('\xa0', ''),
            'year': l.find('span').string,
            'km': l.find('span').next_sibling.string.replace('\xa0', ''),
            'link': f'https://rus.auto24.ee' + link.get('href')
        })
    return new


def save_file(items):
    workbook = xlsxwriter.Workbook(FILE)
    worksheet = workbook.add_worksheet()

    bold = workbook.add_format({'bold': True})

    worksheet.write('A1', 'Марка', bold)
    worksheet.write('B1', 'Цена', bold)
    worksheet.write('C1', 'Год', bold)
    worksheet.write('D1', 'Пробег', bold)
    worksheet.write('E1', 'Ссылка', bold)

    row = 1
    col = 0
    for item in items:
        worksheet.write(row, col, item['model'])
        worksheet.write(row, col + 1, item['price'])
        worksheet.write(row, col + 2, item['year'])
        worksheet.write(row, col + 3, item['km'])
        worksheet.write(row, col + 4, item['link'])
        row += 1

    workbook.close()

    # CSV file saving
    # with open(path, 'w', newline='', encoding="utf-8") as file:
    #     writer = csv.writer(file, delimiter=';')
    #     writer.writerow(['Марка', 'Цена', 'Год', 'Пробег', 'Ссылка'])
    #     for item in items:
    #         writer.writerow([item['model'], item['price'], item['year'], item['km'], item['link']])


def parse():
    URL = input('URL: ')
    URL = URL.strip()
    html = get_link(URL)
    if html.status_code == 200:
        cars = []
        pages_count = get_pages(html.text)
        print(pages_count)

        for page in range((int(pages_count) // 50)):
            print(f'Парсинг страницы {page} из {int(pages_count) // 50}...')
            html = get_link(URL, params={'ak': page * 50})
            cars.extend(get_content(html.text))

            if page == (int(pages_count) // 50) - 1:
                html = get_link(URL, params={'ak': (page + 1) * 50})
                cars.extend(get_content(html.text))

        save_file(cars)
        print('Всего машин - ', len(cars))
        os.startfile(FILE)

    else:
        print('Error')


if __name__ == '__main__':
    parse()
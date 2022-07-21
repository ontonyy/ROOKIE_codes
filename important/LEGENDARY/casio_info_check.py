from bs4 import BeautifulSoup
import requests
from xlsxwriter import *


FILE = 'special_files/casio.xlsx'

def casio_info(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')

    watches = soup.find_all('a', class_='product-item__link')
    casios = []
    for w in watches:
        watch_info = w.text.split()
        watch_info[0] = 'G-SHOCK'
        print(watch_info)
        link = 'https://shop.casio.ru/' + w.get('href')
        print(link)

        casios.append({
            'model': ''.join(watch_info[:2]),
            'price': ''.join(watch_info[2:]),
            'watch_links': link
        })

    save_file(casios)

def save_file(items):
    wb = Workbook(FILE)
    ws = wb.add_worksheet('CASIO')
    bold = wb.add_format({'bold': True})

    ws.write('A1', 'MODEL', bold)
    ws.write('B1', 'PRICE', bold)
    ws.write('C1', 'LINK', bold)

    row = 1
    col = 0
    for item in items:
        ws.write(row, col, item['model'])
        ws.write(row, col + 1, item['price'])
        ws.write(row, col + 2, item['watch_links'])
        row += 1

    wb.close()

if __name__ == '__main__':
    casio_info('https://shop.casio.ru/')
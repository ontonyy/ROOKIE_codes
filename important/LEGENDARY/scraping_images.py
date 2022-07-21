# This site have a limit to downloading some images, roughly 30 images you can download
import requests
import fake_useragent
from bs4 import BeautifulSoup

image_number = 0
storage_num = 1
link = 'https://zastavok.net/'

response = requests.get(f'{link}/1').text
soup = BeautifulSoup(response, 'lxml')
# Page amount
page_num = soup.find('div', class_='ruler').find_all('a')[-2].text


for storage in range(2476):
    response = requests.get(f'{link}/{storage_num}').text
    soup = BeautifulSoup(response, 'lxml')
    block = soup.find('div', class_='block-photo')
    all_images = block.find_all('div', class_='short_full')

    for image in all_images:
        image_link = image.find('a').get('href')
        download_storage = requests.get(f'{link}{image_link}').text
        download_soup = BeautifulSoup(download_storage, 'lxml')
        download_block = download_soup.find('div', class_='image_data').find('div', class_='block_down')
        result_link = download_block.find('a').get('href')

        image_bytes = requests.get(f'{link}{result_link}').content

        with open(f'special_files/scraped_images/{image_number}.png', 'wb') as file:
            file.write(image_bytes)

        image_number += 1
        print(f'Image {image_number}.png/{int(page_num)*18} - successfully downloaded!')
    storage_num += 1
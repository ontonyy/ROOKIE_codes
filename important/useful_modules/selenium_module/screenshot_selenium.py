import os

from selenium import webdriver

def get_screenshot():
    country = input('Weather check screenshot\nPick a country: ')
    link = f'https://openweathermap.org/find?q={country}'

    driver = webdriver.Chrome()
    driver.get(link)

    screen = link.split('=')[-1] + '.png'
    driver.save_screenshot(screen)

    driver.refresh()
    driver.quit()

    os.startfile('C:/main_modules/my_modules/useful_modules/selenium_module/' + screen)

if __name__ == '__main__':
    get_screenshot()

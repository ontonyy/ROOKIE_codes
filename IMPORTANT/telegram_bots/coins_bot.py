from selenium import webdriver
import pickle
import time

options = webdriver.ChromeOptions()
options.headless = True

def coins_check(url):
    driver = webdriver.Chrome(
        r'C:\ROOKIE_codes\projects\IMPORTANT\useful_modules\selenium_module\chromedriver.exe',
        # options=options
    )

    driver.get(url)
    for cookie in pickle.load(open(r'C:\ROOKIE_codes\projects\IMPORTANT\telegram_bots\cookie\session', 'rb')):
        driver.add_cookie(cookie)

    driver.refresh()
    time.sleep(2)
    print('Starting to collect info about coins')
    prices = driver.find_elements_by_class_name('lastprice')
    names = driver.find_elements_by_class_name('bitcoinName')
    percents = driver.find_elements_by_class_name('percentage')
    for n, c, p in zip(names[1:], prices[1:], percents[1:]):
        print(f'{n.text} - {c.text[2:]} euro. Percent: {p.text}')


if __name__ == '__main__':
    coins_check('https://www.worldcoinindex.com/')

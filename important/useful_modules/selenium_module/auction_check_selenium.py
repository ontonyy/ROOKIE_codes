# Auto24 auto-check auction
# ontony <- is me

import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36")

# disable webdriver mode
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(
    executable_path='C:/main_modules/my_modules/useful_modules/selenium_module/chromedriver.exe',
    options=options
)

def vk_func(url):
    try:
        driver.get(url)
        driver.implicitly_wait(10)
        driver.maximize_window()

        driver.implicitly_wait(10)
        driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div/div[3]/div/div/button').click()
        time.sleep(2)

        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        links = soup.find_all('a', class_='row-link')

        new_links = []
        new_links.append(driver.current_url)
        for link in links:
            got_link = 'https://rus.auto24.ee' + link.get('href')
            new_links.append(got_link)

        for l in new_links[1:]:
            time.sleep(2)
            driver.get(l)
            driver.implicitly_wait(5)
            try:
                car = driver.find_element_by_class_name('commonSubtitle')
                print(f'Car is - {car.text}')

                last_days = driver.find_element_by_id('auction-countdown-widget')
                print(f"Days before ending - {last_days.text}")

                driver.implicitly_wait(2)
                best_price = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/form/table/tbody/tr[5]/td[2]/span')
                print(f"Best price - {best_price.text}\n")
            except:
                continue
            finally:
                time.sleep(3)


    except Exception as ex:
        print(f'\n{ex}')
    finally:
        time.sleep(2)
        driver.quit()

if __name__ == '__main__':
    vk_func('https://rus.auto24.ee/kasutatud/nimekiri.php?bn=2&a=100&ae=2&af=50&by=1&ssid=15540755')
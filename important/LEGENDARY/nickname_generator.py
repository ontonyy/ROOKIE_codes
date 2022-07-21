# Nickname generator

import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True

def get_nickname(url):
    try:
        driver = webdriver.Chrome(
            r'C:\ROOKIE_codes\projects\IMPORTANT\useful_modules\selenium_module\chromedriver.exe',
            options=options)
        driver.get(url)
        time.sleep(3)
        driver.implicitly_wait(10)

        names = []
        while len(names) < 100:
            driver.implicitly_wait(2)
            driver.find_element_by_xpath('/html/body/div[3]/section/div/div[1]/div/div/form/div[3]/div/button').click()
            time.sleep(2)
            nicknames = driver.find_elements_by_class_name('tag.tag_result.has-text-weight-bold.has-background-white-bis.is-size-4.is-size-5-mobile.is-size-3-widescreen ')
            for nickname in nicknames:
                names.append(nickname.text)

        for n, x in zip(names, range(1, len(names))):
            print(x * ' ',f"---> {n}")

    except Exception as ex:
        print(ex)
    finally:
        time.sleep(2)
        driver.close()
        driver.quit()

if __name__ == '__main__':
    get_nickname('https://randomus.ru/nickname')

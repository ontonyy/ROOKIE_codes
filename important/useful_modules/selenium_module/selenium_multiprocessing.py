import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from multiprocessing import Pool

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")

# disable webdriver mode
options.add_argument("--disable-blink-features=AutomationControlled")

# Headless mode
# options.headless = True

url_links = ["https://stackoverflow.com", "https://instagram.com", "https://vk.com"]

def get_data(url):
    try:
        driver = webdriver.Chrome(
            executable_path='C:/main_modules/my_modules/useful_modules/selenium_module/chromedriver.exe',
            options=options
        )
        driver.get(url=url)
        time.sleep(5)
        driver.save_screenshot(f"media/{url.split('//')[1]}.png")

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

if __name__ == '__main__':
    p = Pool(processes=3)
    p.map(get_data, url_links)
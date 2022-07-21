import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from auth_data import vk_password, vk_phone


options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")

# disable webdriver mode
options.add_argument("--disable-blink-features=AutomationControlled")

# Headless mode
options.headless = True

driver = webdriver.Chrome(
    executable_path='C:/main_modules/my_modules/useful_modules/selenium_module/chromedriver.exe',
    options=options
)


def vk_func(url):
    try:
        driver.get(url)
        time.sleep(5)

        print('Passing authentication...')
        phone_input = driver.find_element_by_id('index_email')
        phone_input.clear()
        phone_input.send_keys(vk_phone)
        time.sleep(3)

        password_input = driver.find_element_by_id('index_pass')
        password_input.clear()
        password_input.send_keys(vk_password)
        time.sleep(3)
        password_input.send_keys(Keys.ENTER)
        time.sleep(5)

        print('Going into videos playlist...')
        videos_link = driver.find_element_by_id("l_vid").click()
        time.sleep(5)

        print('Watching a video a little bit...')
        video_play = driver.find_element_by_class_name('video_item_controls').click()
        time.sleep(5)

    except Exception as ex:
        print(ex)
    finally:
        time.sleep(5)
        print('End of the code...')
        driver.quit()

if __name__ == '__main__':
    vk_func('https://vk.com/')
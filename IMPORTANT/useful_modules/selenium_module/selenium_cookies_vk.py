import pickle
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from auth_data import vk_password, vk_phone


options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")

# disable webdriver mode
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(
    executable_path=
    r'C:\ROOKIE_codes\projects\IMPORTANT\useful_modules\selenium_module\chromedriver.exe',
    options=options)

try:
    # driver.get('https://vk.com/')
    # time.sleep(5)
    #
    #
    # phone_input = driver.find_element_by_id('index_email')
    # phone_input.clear()
    # phone_input.send_keys(vk_phone)
    # time.sleep(3)
    #
    # password_input = driver.find_element_by_id('index_pass')
    # password_input.clear()
    # password_input.send_keys(vk_password)
    # time.sleep(3)
    # password_input.send_keys(Keys.ENTER)
    # time.sleep(5)
    #
    # news_link = driver.find_element_by_id("l_nwsf").click()
    # time.sleep(5)
    #
    # # cookies
    # pickle.dump(driver.get_cookies(), open(f'{vk_phone}_cookies', 'wb'))

    driver.get('https://vk.com/')
    time.sleep(5)

    for cookie in pickle.load(open(f'{vk_phone}_cookies', 'rb')):
        driver.add_cookie(cookie)

    time.sleep(5)
    driver.refresh()
    time.sleep(10)

except Exception as ex:
    print(ex)
finally:
    time.sleep(5)
    driver.quit()

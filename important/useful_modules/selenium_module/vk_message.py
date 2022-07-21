import pickle
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from auth_data import vk_password, vk_phone


options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")

# disable webdriver mode
options.add_argument("--disable-blink-features=AutomationControlled")

def message(url):
    try:
        driver = webdriver.Chrome(executable_path=r'C:\ROOKIE_codes\projects\IMPORTANT\useful_modules\selenium_module\chromedriver.exe', options=options)

        driver.get(url)
        driver.implicitly_wait(3)

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

        message_link = driver.find_element_by_id("l_msg").click()
        time.sleep(2)

        person_click = driver.find_element_by_xpath('/html/body/div[12]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div[2]/ul/li[2]').click()
        time.sleep(2)

        string_to = driver.find_element_by_id('im_editable0')
        string_to.click()
        string_to.clear()
        string_to.send_keys('Пиздец пушечка залетела, кноклбол' + Keys.ENTER)
        time.sleep(3)

    except Exception as ex:
        print(ex)
    finally:
        time.sleep(5)
        driver.quit()

if __name__ == '__main__':
    message('https://vk.com/')

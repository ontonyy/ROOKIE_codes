import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def insta_into(url):
    name = input("Username: ")
    parool = input("Password: ")
    driver = webdriver.Chrome('C:/main_modules/my_modules/useful_modules/selenium_module/chromedriver.exe')
    driver.get(url)
    driver.maximize_window()

    driver.find_element_by_xpath('/html/body/div[3]/div/div/button[1]').click()
    time.sleep(2)

    try:
        username = driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')
        username.send_keys(name)

        password = driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')
        password.send_keys(parool)

        # Enter to insta with data
        driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div').click()


        time.sleep(3)
        # Not now saving data
        driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()

        time.sleep(3)
        # Turn off notifications
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()

    except Exception as ex:
        time.sleep(2)
        driver.quit()
        print('\nTry again!\n')
        insta_into('https://www.instagram.com/')


    finally:
        time.sleep(3)
        driver.quit()

if __name__ == '__main__':
    insta_into('https://www.instagram.com/')
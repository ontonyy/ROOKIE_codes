# Project to enter to your mail and check how many messages and first message check
# Auto gmail check

import time
from selenium import webdriver
import os
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import InvalidSessionIdException


def go_sisse():
    name = input('Enter your mail: ')
    parool = input('Enter your password: ')

    global driver
    driver = webdriver.Chrome()
    driver.get('https://accounts.google.com/ServiceLogin/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
    time.sleep(2)

    login = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')
    login.send_keys(name)
    time.sleep(2)

    driver.find_element_by_class_name('VfPpkd-vQzf8d').click()
    time.sleep(2)

    try:
        driver.find_element_by_class_name('o6cuMc')

    except NoSuchElementException:
        time.sleep(2)
        password = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
        password.send_keys(parool)
        time.sleep(1)

        driver.find_element_by_class_name('VfPpkd-vQzf8d').click()

        try:
            driver.find_element_by_class_name('EjBTad')

        except NoSuchElementException:
            time.sleep(5)

            all_messages = driver.find_element_by_class_name('bsU').text
            print(f'\nIn mail only {all_messages} messages')

            last_sender = driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div[8]/div/div[1]/div[3]/div/table/tbody/tr[1]/td[4]/div[2]/span/span').text
            print(f"\nLast sender is {last_sender}")

            driver.maximize_window()
            time.sleep(2)

            driver.find_element_by_xpath(
                '/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div[8]/div/div[1]/div[3]/div/table/tbody/tr[1]').click()
            time.sleep(5)

            driver.close()
        else:
            driver.close()
            print('\nPassword failed. TRY AGAIN.')
            go_sisse()

    else:
        driver.close()
        print('\nLogin failed. TRY AGAIN.')
        go_sisse()


if __name__ == '__main__':
    go_sisse()
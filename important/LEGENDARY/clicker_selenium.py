import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


# Common clicker, not fast, but not slow
def make_clicks(url):
    driver = webdriver.Chrome(
        'C:/main_modules/my_modules/useful_modules/selenium_module/chromedriver.exe')
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(2)
    driver.find_element_by_xpath('/html/body/div[1]/div/a[1]').click()

    cookie = driver.find_element_by_id('bigCookie')
    cookie_count = driver.find_element_by_id('cookies')

    items = [driver.find_element_by_id(
        'productPrice' + str(i)) for i in range(1, -1, -1)]

    actions = ActionChains(driver)
    actions.click(cookie)

    for i in range(5000):
        actions.perform()
        count = int(cookie_count.text.split(' ')[0])
        print(count)
        for item in items:
            value = int(item.text)
            if value <= count:
                upgrade_actions = ActionChains(driver)
                upgrade_actions.move_to_element(item)
                upgrade_actions.click()
                upgrade_actions.perform()

    driver.quit()


# Fastest clicker than function above
def fast_clicks(url):
    driver = webdriver.Chrome('C:/main_modules/my_modules/useful_modules/selenium_module/chromedriver.exe')
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(2)
    driver.find_element_by_xpath('/html/body/div[1]/div/a[1]').click()

    cookie = driver.find_element_by_id('bigCookie')
    cookie_count = driver.find_element_by_id('cookies')

    items = [driver.find_element_by_id('productPrice' + str(i)) for i in range(1, -1, -1)]


    while int(cookie_count.text.split(' ')[0]) != 2000:
        cookie.click()
        for item in items:
            print(item.text)
            value = int(item.text)

            if value == int(cookie_count.text.split(' ')[0]):
                upgrade_actions = ActionChains(driver)
                upgrade_actions.move_to_element(item)
                upgrade_actions.click()
                upgrade_actions.perform()

    driver.quit()


if __name__ == '__main__':
    # make_clicks('https://orteil.dashnet.org/cookieclicker/')
    fast_clicks('https://orteil.dashnet.org/cookieclicker/')

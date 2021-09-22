import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def you_video(url):
    request = input('Youtube search: ')

    driver = webdriver.Chrome(
        r'C:\ROOKIE_codes\projects\IMPORTANT\useful_modules\selenium_module\chromedriver.exe'
    )
    driver.get(url)

    driver.find_element_by_xpath('/html/body/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div[1]/div/button/span').click()

    time.sleep(5)
    search = driver.find_element_by_class_name('style-scope ytd-searchbox')
    search.send_keys(request)
    search.send_keys(Keys.RETURN)
    time.sleep(5)

    try:
        wait = WebDriverWait(driver, 10)

        element = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer')))
        element.click()

        time.sleep(5)

    except:
        time.sleep(5)
        driver.close()

if __name__ == '__main__':
    you_video('https://www.youtube.com/')
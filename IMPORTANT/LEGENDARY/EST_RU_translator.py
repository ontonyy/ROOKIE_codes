# Estonian or Russian word translator

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from tkinter import *
from tkinter import messagebox

def main(url):
    # Translated word in russian to estonia
    user_word = str(input('Some word in Russia: '))
    driver = webdriver.Chrome('C:/main_modules/my_modules/useful_modules/selenium_module/chromedriver.exe')
    driver.get(url)
    driver.maximize_window()
    time.sleep(2)


    word = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div/div/form/div[1]/input[1]')
    word.send_keys(user_word)
    word.send_keys(Keys.RETURN)

    try:
        driver.find_element_by_xpath('/html/body/div[4]/main/div/span').text
    except:

        try:
            wait = WebDriverWait(driver, 5)
            element = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/form/div[2]/button[4]')))
            element.click()
        except:
            driver.close()

    finally:
        driver.close()
        root = Tk()

        response = messagebox.askquestion('Wrong word', 'TRY AGAIN, or not?')

        while True:
            if response == 'yes':
                main('https://sonaveeb.ee/')
            elif response == 'no':
                break

        root.mainloop()

if __name__ == '__main__':
    main('https://sonaveeb.ee/')

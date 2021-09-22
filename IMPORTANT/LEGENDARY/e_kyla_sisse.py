from selenium import webdriver
import time
import pyautogui as gui
from tkinter import *
from tkinter import messagebox
import os 
import keyboard
from threading import Thread

root = Tk()
root.withdraw()
messagebox.showinfo('INFO', 'If anything, just press \'Q\' to exit!')
time.sleep(3)


try:
    os.listdir('keys_eKyla.txt')
    print('File is found')
except FileNotFoundError:
    nickname = input('Kasutaja: ')
    parool = input('Parool: ')
    with open('keys_eKyla.txt', 'w+') as f:
        f.write(nickname + '\n')
        f.write(parool)
except NotADirectoryError:
    with open('keys_eKyla.txt', 'r') as f:
        nickname, parool = f.readlines()

print('Start working...')

def key_check():
    print('Key is check')
    while True:
        if keyboard.is_pressed('q'):
            driver.quit()
            break
        else:
            continue

def get_sisse(url):
    global driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path=
    r'C:\ROOKIE_codes\projects\IMPORTANT\useful_modules\selenium_module\chromedriver.exe', options=options)
    driver.get(url)

    try:
        while not keyboard.is_pressed('q'):
            with open('keys_eKyla.txt', 'r') as f:
                nickname, parool = f.readlines()
            gui.PAUSE = 1.5

            gui.hotkey('winleft', 'up')

            name = driver.find_element_by_xpath(
                '/html/body/form/table/tbody/tr[2]/td/div/div[2]/table[1]/tbody/tr[1]/td/input')

            name.send_keys(nickname[:-1])

            time.sleep(2)
            password = driver.find_element_by_xpath(
                '/html/body/form/table/tbody/tr[2]/td/div/div[2]/table[1]/tbody/tr[2]/td/input'
            )

            password.send_keys(parool)

            time.sleep(2)
            driver.find_element_by_xpath(
                '/html/body/form/table/tbody/tr[2]/td/div/div[2]/table[2]/tbody/tr[2]/td/input'
            ).click()

            time.sleep(1)

            driver.find_element_by_xpath(
                '/html/body/form/table/tbody/tr[2]/td/div/div[2]/table[3]/tbody/tr[1]/td[1]/input'
            ).click()

            time.sleep(2)

            root.mainloop()
            if keyboard.is_pressed('q'):
                driver.quit()
                break
            
    except Exception as ex:
        print(ex)

if __name__ == '__main__':
    t1 = Thread(target = key_check).start()
    t2 = Thread(target = get_sisse, args=['https://e-kyla.campusttu.ee/',]).start()

    
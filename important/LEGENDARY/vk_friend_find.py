# Check some friend in other friends

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from collections import deque

# Input data
vk_phone = input('Enter your phone: ')
vk_password = input('Enter your password: ')

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")

# disable webdriver mode
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(
    executable_path='C:/main_modules/my_modules/useful_modules/selenium_module/chromedriver.exe',
    options=options
)

def friend_check(url):
    try:
        # Go into vkontakte
        driver.get(url)
        time.sleep(5)

        # Data input
        phone_input = driver.find_element_by_id('index_email')
        phone_input.clear()
        phone_input.send_keys(vk_phone)
        driver.implicitly_wait(3)

        password_input = driver.find_element_by_id('index_pass')
        password_input.clear()
        password_input.send_keys(vk_password)
        driver.implicitly_wait(3)

        password_input.send_keys(Keys.ENTER)
        driver.implicitly_wait(5)

        driver.maximize_window()

        # Go to your friends list
        friend_click = driver.find_element_by_id("l_fr").click()
        time.sleep(5)

        # Check all friends info, and their links
        count = 0
        while count < 10:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            count += 1

        time.sleep(1)
        friends = driver.find_elements_by_xpath('//div[@class="friends_field friends_field_title"]/a')


        friends_dict = {}
        names = []
        links = []

        # Names and links here
        for f in friends:
            names.append(f.text.split(' ')[0])
            links.append(f.get_attribute('href'))

        # Make a dictionary with deque(), to easier changing
        friends_dict['Anton'] = names

        search_queue = deque()
        search_queue += friends_dict['Anton']
        searched = []

        time.sleep(5)
        # breadth-first search(check chapter 6 in book 'grokaem algorithms')
        while search_queue:
            for link, name in zip(links, names):
                if name not in searched:
                    # Finding someone in friends list
                    if name == 'Jelena':
                        driver.get(link)
                        time.sleep(3)
                        print(len(names))
                        print(f'\n{name} - > {link}')
                        driver.close()
                        driver.quit()
                        break
                    else:
                        try:
                            # Get friends link, and appending their friends
                            driver.implicitly_wait(10)
                            driver.get(link)

                            driver.implicitly_wait(10)
                            driver.find_element_by_xpath('/html/body/div[12]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/div/div[2]/aside[2]/div/a[2]/div').click()

                            time.sleep(2)
                            count = 0
                            while count < 10:
                                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                                count += 1
                            time.sleep(2)

                            driver.implicitly_wait(10)
                            friends = driver.find_elements_by_xpath('//div[@class="friends_field friends_field_title"]/a')

                            for f in friends:
                                n = f.text.split(' ').pop(0)
                                l = f.get_attribute('href')
                                if n not in searched:
                                    names.append(n)
                                    links.append(l)

                            # Appending info to deque
                            search_queue += friends_dict[name]
                            searched.append(name)
                            time.sleep(5)

                            # Previous checked friends deleting
                            del names[0]
                            del links[0]

                        except:
                            continue
                else:
                    continue

                print('No one found:(')
                break

    except Exception as ex:
        print(ex)

    finally:
        time.sleep(5)
        driver.quit()

if __name__ == '__main__':
    friend_check('https://vk.com/')

# This a code to write invisible message to your own or someone gmail, this is really cool thing, that i made
# More easier write this program with smtplib module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import InvalidSessionIdException
import time

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36")

# disable webdriver mode
options.add_argument("--disable-blink-f eatures=AutomationControlled")

# You can make this programm invisible
options.headless = True

# Data for entering and message
name = input('Enter your mail: ')
parool = input('Enter your password: ')
theme = input('\n-> Enter a topic: ')
info = input('-> Enter a message: ')

start = time.time()

driver = webdriver.Chrome(
    executable_path='C:/main_modules/my_modules/useful_modules/selenium_module/chromedriver.exe',
    options=options
)


def message_send(url):
    try:
        print('Enter to a site')
        driver.get(url)
        driver.maximize_window()

        # Authorization in gmail with your data
        login = driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')
        login.send_keys(name + Keys.ENTER)
        time.sleep(2)
        print('Authorization in gmail...')

        # This weird block, because if login is INVALID, if not (except)
        try:
            driver.find_element_by_class_name('o6cuMc')

        except NoSuchElementException:
            driver.implicitly_wait(2)

            password = driver.find_element_by_xpath(
                '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
            password.send_keys(parool + Keys.ENTER)
            time.sleep(1)

            # This strange block, because if password is INVALID, if not (except)
            try:
                driver.find_element_by_class_name('EjBTad')

            except NoSuchElementException:
                time.sleep(2)


                # Click to message "Write"
                driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div').click()
                time.sleep(2)

                # Person to whom going message
                mail = driver.find_element_by_class_name('vO')
                mail.send_keys(name)
                driver.implicitly_wait(2)

                # Topic to message
                topic = driver.find_element_by_class_name('aoT')
                topic.send_keys(theme)
                time.sleep(2)

                print('Message sending...')
                # Some message
                message = driver.find_element_by_class_name('tS-tW')
                message.send_keys(info)
                time.sleep(1)

                # Click a send button
                driver.find_element_by_class_name('T-I.J-J5-Ji.aoO.v7.T-I-atl.L3').click()
                time.sleep(2)

                print('---> Programm ending... <---')
                driver.close()
            else:
                driver.close()
                print('\nPassword failed. TRY AGAIN.')
                message_send(url)

        else:
            driver.close()
            print('\nLogin failed. TRY AGAIN.')
            message_send(url)

    except Exception as ex:
        print(ex)

    except InvalidSessionIdException:
        driver.close()

    finally:
        driver.quit()

if __name__ == '__main__':
    message_send('https://accounts.google.com/ServiceLogin/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
    end = time.time()
    print(f'\nThis code taked a --- {round(end - start, 2)} seconds(s)')
import time

from selenium import webdriver

def main():
    driver = webdriver.Chrome()
    driver.get('https://proghub.ru/developer')
    time.sleep(2)
    
    btn_elem = driver.find_element_by_class_name('btn-primary.btn.btn-block')
    btn_elem.click()
    time.sleep(2)

if __name__ == '__main__':
    main()
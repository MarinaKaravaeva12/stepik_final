import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/simple_form_find_task.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input_1 = browser.find_element(By.NAME,'first_name')
    input_1.send_keys('Marina')

    input_2 = browser.find_element(By.NAME, 'last_name')
    input_2.send_keys('Karavaeva')

    input_3 = browser.find_element(By.CLASS_NAME,'city')
    input_3.send_keys('Gomel')

    input_4 = browser.find_element(By.ID, 'country')
    input_4.send_keys('Belarus')

    button = browser.find_element(By.ID, 'submit_button')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
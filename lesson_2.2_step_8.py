import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import os

link = 'https://suninjuly.github.io/file_input.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)

    elements = browser.find_elements(By.CSS_SELECTOR,'input[type="text"]')
    for element in elements:
        element.send_keys('test')

    current_dir = os.path.abspath(os.path.dirname(__file__))

    file_path = os.path.join(current_dir,'test.txt')
    browser.find_element(By.ID,'file').send_keys(file_path)

    browser.find_element(By.TAG_NAME,'button').click()

finally:
    time.sleep(5)
    browser.quit()
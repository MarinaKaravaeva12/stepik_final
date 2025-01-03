import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/huge_form.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    elements = browser.find_elements(By.CSS_SELECTOR, 'input[type="text"]')
    for element in elements:
        element.send_keys('1')

    button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-default')
    button.click()

finally:
    time.sleep(30)
    browser.quit()
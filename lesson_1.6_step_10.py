import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/registration1.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    elements = browser.find_elements(By.CSS_SELECTOR, 'input[required]')

    for element in elements:
        element.send_keys('test')

    button = browser.find_element(By.XPATH,'//button[@class="btn btn-default"]')
    button.click()
    time.sleep(3)
    text_h1 = browser.find_element(By.TAG_NAME,'h1')
    assert text_h1.text == 'Congratulations! You have successfully registered!'
finally:
    time.sleep(5)
    browser.quit()
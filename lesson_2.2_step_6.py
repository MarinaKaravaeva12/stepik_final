import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math


link = 'https://suninjuly.github.io/execute_script.html'

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element(By.ID,'input_value').text)

    result = calc(x)

    browser.find_element(By.ID,'answer').send_keys(result)

    checkbox = browser.find_element(By.ID,'robotCheckbox')
    browser.execute_script('return arguments[0].scrollIntoView(true)',checkbox)
    checkbox.click()

    radio = browser.find_element(By.ID,'robotsRule')
    radio.click()

    browser.find_element(By.TAG_NAME,'button').click()

finally:
    time.sleep(5)
    browser.quit()
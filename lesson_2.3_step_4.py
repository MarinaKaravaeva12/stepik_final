import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math

link = 'https://suninjuly.github.io/alert_accept.html'

def calc(x):
    return math.log(abs(12*math.sin(x)))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.TAG_NAME,'button').click()
    confirm = browser.switch_to.alert
    # time.sleep(2)
    # confirm.dismiss()
    confirm.accept()

    x = int(browser.find_element(By.ID,'input_value').text)
    result = calc(x)

    browser.find_element(By.ID,'answer').send_keys(result)
    browser.find_element(By.TAG_NAME,'button').click()

finally:
    time.sleep(5)
    browser.quit()

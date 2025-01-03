import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
    return math.log(abs(12*math.sin(x)))

link = 'https://suninjuly.github.io/redirect_accept.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.TAG_NAME,'button').click()

    browser.switch_to.window(browser.window_handles[1])

    x = int(browser.find_element(By.ID,'input_value').text)
    result = calc(x)

    browser.find_element(By.ID,'answer').send_keys(result)
    browser.find_element(By.TAG_NAME,'button').click()

finally:
    time.sleep(5)
    browser.quit()
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = 'https://suninjuly.github.io/math.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    tag_x = browser.find_element(By.ID,'input_value')
    x = tag_x.text
    y = calc(x)

    input_answer = browser.find_element(By.ID,'answer')
    input_answer.send_keys(y)

    checkbox_robot = browser.find_element(By.CSS_SELECTOR,'[for = "robotCheckbox"]')
    checkbox_robot.click()

    radio_button_robots = browser.find_element(By.ID,'robotsRule')
    radio_button_robots.click()

    button = browser.find_element(By.CSS_SELECTOR,'.btn.btn-default')
    button.click()

finally:
    time.sleep(5)
    browser.quit()

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

import math
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = 'https://suninjuly.github.io/get_attribute.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    image_treasure = browser.find_element(By.ID,'treasure')
    image_value = image_treasure.get_attribute('valuex')

    y = calc(int(image_value))

    input = browser.find_element(By.ID, 'answer')
    input.send_keys(y)

    checkbox_robot = browser.find_element(By.ID,'robotCheckbox')
    checkbox_robot.click()

    radio_button_robots = browser.find_element(By.ID,'robotsRule')
    radio_button_robots.click()

    button = browser.find_element(By.CSS_SELECTOR,'.btn.btn-default')
    button.click()

finally:
    time.sleep(5)
    browser.quit()
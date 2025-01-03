import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    return math.log(abs(12*math.sin(x)))

link = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    text = WebDriverWait(browser,12).until(
        EC.text_to_be_present_in_element((By.ID,'price'),'$100')
    )
    browser.find_element(By.ID,'book').click()

    x = int(browser.find_element(By.ID,'input_value').text)
    result = calc(x)
    browser.find_element(By.ID,'answer').send_keys(result)
    browser.find_element(By.ID,'solve').click()
finally:
    time.sleep(5)
    browser.quit()
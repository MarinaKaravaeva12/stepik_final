import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


link = 'https://suninjuly.github.io/selects2.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID,'num1').text
    num2 = browser.find_element(By.ID,'num2').text

    sum = int(num1)+int(num2)
    print(sum)
    value_sum = str(sum)
    select = Select(browser.find_element(By.TAG_NAME,'select'))
    select.select_by_value(value_sum)

    browser.find_element(By.XPATH,'//button[@class="btn btn-default"]').click()

finally:
    time.sleep(5)
    browser.quit()
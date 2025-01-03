import time

from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://suninjuly.github.io/selects1.html')
browser.execute_script('alert("Hello!"); document.title = "test"')
time.sleep(5)
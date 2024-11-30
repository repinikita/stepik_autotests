from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

def sum(x, y):
  return str((int(x)+int(y)))

try: 
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, "num1")
    x = x.text
    y = browser.find_element(By.ID, "num2")
    y = y.text
    z = sum(x, y)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(z))

    button = browser.find_element(By.CSS_SELECTOR, "body > div > form > button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # атрибут .text для найденного элемента

    x_element = browser.find_element_by_id('num1')
    x = x_element.text

    y_element = browser.find_element_by_id('num2')
    y = y_element.text

    num1 = int(x)
    num2 = int(y)
    sum_el = num1 + num2

    select = Select(browser.find_element_by_tag_name('select'))
    select.select_by_visible_text(str(sum_el))

    # Отправляем заполненную форму
    button = browser.find_element_by_tag_name("button")
    button.click()

    # ждем загрузки страницы
    time.sleep(1)

    print("УРА! I did it!!!")

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    # пустая строка
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # атрибут .text для найденного элемента

    valuex_radio = browser.find_element_by_id('treasure')
    x_element = valuex_radio.get_attribute('valuex')
    x = x_element
    y = calc(x)

    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)

    # Код для чекбокса и радиобатонна
    option1 = browser.find_element_by_css_selector("#robotsRule")
    option1.click()
    option2 = browser.find_element_by_css_selector("#robotCheckbox")
    option2.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # ждем загрузки страницы
    time.sleep(1)

    print("УРА! I did it!!!")

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

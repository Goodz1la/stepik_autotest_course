from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    option1 = browser.find_element_by_css_selector("#robotsRule")
    option1.click()
    option2 = browser.find_element_by_css_selector("#robotCheckbox")
    option2.click()

    button.click()

    assert True
    time.sleep(1)
    print("УРА! I did it!!!")

finally:
    time.sleep(10)
    browser.quit()

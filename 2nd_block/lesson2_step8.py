from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector('.form-group input[name="firstname"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector('.form-group input[name="lastname"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector('.form-group input[name="email"]')
    input3.send_keys("dff@fgjkf.sa")

    add_file = browser.find_element_by_css_selector('input[type="file"]')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'text.txt')
    add_file.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

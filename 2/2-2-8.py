from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1=browser.find_element_by_css_selector("[name='firstname']")
    input1.send_keys("1")
    input2=browser.find_element_by_css_selector("[name='lastname']")
    input2.send_keys("2")
    input3=browser.find_element_by_css_selector("[name='email']")
    input3.send_keys("3")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, '2-2-8.txt')
    file=browser.find_element_by_id("file")
    file.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
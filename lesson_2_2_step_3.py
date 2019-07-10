from selenium import webdriver
import math

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

num1 = browser.find_element_by_id("num1")
num1_value = num1.text
num2 = browser.find_element_by_id("num2")
num2_value = num2.text
y = str(int(num1_value) + int(num2_value))

from selenium.webdriver.support.ui import Select
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_visible_text(y) 

button = browser.find_element_by_css_selector("button.btn")
button.click()

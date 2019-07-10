from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

x = browser.find_element_by_id("input_value")
x_value = x.text

y = calc(x_value)

browser.execute_script("window.scrollBy(0, 100);")

input1 = browser.find_element_by_css_selector("#answer")
input1.send_keys(y)

option1 = browser.find_element_by_id("robotCheckbox")
option1.click()

option2 = browser.find_element_by_id("robotsRule")
option2.click()

button = browser.find_element_by_css_selector("button.btn")
button.click()

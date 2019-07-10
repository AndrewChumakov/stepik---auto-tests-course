from selenium import webdriver
import os 

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

name = browser.find_element_by_name("firstname")
name.send_keys("qwer")

sername = browser.find_element_by_name("lastname")
sername.send_keys("asd")

mail = browser.find_element_by_name("email")
mail.send_keys("zxc")

current_dir = os.path.abspath(os.path.dirname(__file__))    
file_path = os.path.join(current_dir, 'test.txt')
element = browser.find_element_by_name("file")         
element.send_keys(file_path)

button = browser.find_element_by_css_selector("button.btn")
button.click()

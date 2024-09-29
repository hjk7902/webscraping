import os
html_file = os.getcwd() + "/sample2.html"

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# 브라우저 종료 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("file:///" + html_file)

login_form = driver.find_element(by='id', value='loginForm')
print(login_form)

username = driver.find_element(by='name', value='username')
username.send_keys("Hello")

password = driver.find_element(by='name', value='password')
password.send_keys("1234567890")

link = driver.find_element(by='link text', value='자바전문가그룹')
# link = driver.find_element(by='partial link text', value='자바')
link.click()

driver.back()

heading1 = driver.find_element(by='tag name', value='h1')
print(heading1.text)

content = driver.find_element(by='class name', value='content')
print(content.text)

content = driver.find_element(by='css selector', value='p.content')
print(content.text)

driver.close()
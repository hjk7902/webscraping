from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.python.org/")
driver.implicitly_wait(5) # 초 단위
menu_list = driver.find_elements(By.CSS_SELECTOR,
                    value="nav#mainnav > ul.navigation > li > a")
for menu in menu_list:
    print(menu.text)
driver.close()
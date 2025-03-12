import selenium
print(selenium.__version__)
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.python.org')

input_el = driver.find_element(by='id', value='id-search-field')
# from selenium.webdriver.common.by import By
# input_el = driver.find_element(by=By.ID, value='id-search-field')
# input_el = driver.find_element(by='css selector', value='#id-search-field')
input_el.send_keys("pycon")

from selenium.webdriver.common.keys import Keys
input_el.send_keys(Keys.RETURN)

from selenium.webdriver.common.by import By
result_list = driver.find_elements(by=By.CSS_SELECTOR, value='form li h3 > a')
for result in result_list:
    print(result.text)

driver.close()
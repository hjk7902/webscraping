import selenium
print(selenium.__version__)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 브라우저 종료 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.python.org')

driver.close()
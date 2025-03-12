from selenium.webdriver import Chrome
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
# import time

driver = Chrome()
driver.get("https://www.weather.go.kr/w/index.do")
# time.sleep(10)

# driver.implicitly_wait(3) # 페이지가 모두 로드될 때 까지 최대 3초 대기
wait = WebDriverWait(driver, 3)
# element = driver.find_element(by='css selector', value='div#current-weather span.tmp')
element = wait.until(
    EC.presence_of_element_located(('css selector', 'div#current-weather span.tmp'))
)
print(element.text)
driver.close()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.weather.go.kr/w/index.do")

wait = WebDriverWait(driver, 5) # 최대 5초까지 대기
element = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR,
                                    "div#current-weather span.tmp"))
)
print(element.text)

driver.close()
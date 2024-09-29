from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.g2b.go.kr/index.jsp")

업무구분 = Select(driver.find_element(by=By.ID, value='taskClCds'))
업무구분.select_by_value('3')

# 공고명 = driver.find_element(by=By.ID, value='bidNm')
# 공고명.send_keys('인공지능')

공고일최근1개월 = driver.find_element(by=By.ID, value='setMonth1_1')
공고일최근1개월.click()

공고기관 = driver.find_element(by=By.ID, value='instNm')
공고기관.send_keys('과학기술정보통신부')

참가제한지역 = Select(driver.find_element(by=By.ID, value='area'))
참가제한지역.select_by_value('11')

검색버튼 = driver.find_element(by=By.CSS_SELECTOR, value='dd.fr .btn_dark strong')
검색버튼.click()

하단프레임 = driver.find_element(by=By.CSS_SELECTOR, value='frameset frame#sub')
print(하단프레임)

driver.switch_to.frame(하단프레임)
콘텐츠프레임 = driver.find_element(by=By.CSS_SELECTOR, value='frame[name=main]')
print(콘텐츠프레임)

driver.switch_to.frame(콘텐츠프레임)
입찰공고목록 = driver.find_elements(by=By.CSS_SELECTOR, value='#resultForm table tbody tr')
print(len(입찰공고목록))

for 입찰공고 in 입찰공고목록:
    공고 = 입찰공고.find_elements(by=By.TAG_NAME, value='td')
    공고번호_차수 = 공고[1].text
    공고명 = 공고[3].text
    공고주소 = 공고[3].find_element(by=By.TAG_NAME, value='a')
    URL = 공고주소.get_property('href')
    print(f'공고번호-차수: {공고번호_차수}, 공고명: {공고명}, URL: {URL}')

driver.close()
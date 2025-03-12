from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from bs4 import BeautifulSoup
import time


def setup_driver():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    return driver


def search_bids(driver):
    driver.get("https://www.g2b.go.kr/index.jsp")

    # 업무구분 선택
    업무구분 = Select(driver.find_element(By.ID, 'taskClCds'))
    업무구분.select_by_value('3')  # 공사

    # 최근 1개월 선택
    공고일최근1개월 = driver.find_element(By.ID, 'setMonth1_1')
    공고일최근1개월.click()

    # 공고기관 입력
    공고기관 = driver.find_element(By.ID, 'instNm')
    공고기관.send_keys('과학기술정보통신부')

    # 참가제한지역 선택
    참가제한지역 = Select(driver.find_element(By.ID, 'area'))
    참가제한지역.select_by_value('11')  # 서울

    # 검색 버튼 클릭
    검색버튼 = driver.find_element(By.CSS_SELECTOR, 'dd.fr .btn_dark strong')
    검색버튼.click()

def get_bid_info(driver):
    하단프레임 = driver.find_element(by=By.CSS_SELECTOR, value='frameset frame#sub')
    driver.switch_to.frame(하단프레임)
    콘텐츠프레임 = driver.find_element(by=By.CSS_SELECTOR, value='frame[name=main]')
    driver.switch_to.frame(콘텐츠프레임)
    입찰공고목록 = driver.find_elements(By.CSS_SELECTOR, "#resultForm table tbody tr")
    print(len(입찰공고목록))
    for 입찰공고 in 입찰공고목록:
        공고 = 입찰공고.find_elements(By.TAG_NAME, 'td')
        공고번호_차수 = 공고[1].text
        공고명 = 공고[3].text
        공고주소 = 공고[3].find_element(By.TAG_NAME, 'a')
        URL = 공고주소.get_property('href')

        print(f'공고번호-차수: {공고번호_차수}, 공고명: {공고명}')

        # 상세 페이지에서 추정금액 가져오기
        response = requests.get(URL)
        soup = BeautifulSoup(response.content, 'html.parser')
        추정금액요소 = soup.select_one('div#container > div:nth-of-type(9)')
        if 추정금액요소:
            추정금액 = 추정금액요소.select_one('table tr:nth-of-type(2) td:nth-of-type(1)')
            if 추정금액:
                print(f'추정금액: {추정금액.text.strip()}')
            else:
                print('추정금액을 찾을 수 없습니다.')
        else:
            print('추정금액 정보를 포함하는 요소를 찾을 수 없습니다.')

        print('-' * 50)

        time.sleep(1)  # 서버 부하를 줄이기 위한 대기 시간


def main():
    driver = setup_driver()
    try:
        search_bids(driver)
        get_bid_info(driver)
    except Exception as e:
        print(e)
    finally:

        driver.quit()


if __name__ == "__main__":
    main()
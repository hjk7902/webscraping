from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.g2b.go.kr/")
actions = ActionChains(driver)

wait = WebDriverWait(driver, 5)
입찰메뉴 = wait.until(EC.element_to_be_clickable((By.ID, 'mf_wfm_gnb_wfm_gnbMenu_genDepth1_1_btn_menuLvl1_span')))
# 입찰메뉴 = driver.find_element(by=By.ID, value='mf_wfm_gnb_wfm_gnbMenu_genDepth1_1_btn_menuLvl1_span')
actions.move_to_element(입찰메뉴).click().perform()

입찰공고목록메뉴 = wait.until(EC.element_to_be_clickable((By.ID, 'mf_wfm_gnb_wfm_gnbMenu_genDepth1_1_genDepth2_0_genDepth3_0_btn_menuLvl3_span')))
# 입찰공고목록메뉴 = driver.find_element(by=By.ID, value='mf_wfm_gnb_wfm_gnbMenu_genDepth1_1_genDepth2_0_genDepth3_0_btn_menuLvl3_span')
actions.move_to_element(입찰공고목록메뉴).click().perform()

상세조건버튼 = wait.until(EC.element_to_be_clickable((By.ID, 'wq_uuid_2241_btnSearchToggle')))
actions.move_to_element(상세조건버튼).click().perform()

전체버튼 = wait.until(EC.element_to_be_clickable((By.ID, 'mf_wfm_container_tacBidPbancLst_contents_tab2_body_chkBidPbancSrchTyCd_input_0')))
actions.move_to_element(전체버튼).click().perform()

공사버튼 = wait.until(EC.element_to_be_clickable((By.ID, 'mf_wfm_container_tacBidPbancLst_contents_tab2_body_chkBidPbancSrchTyCd_input_4')))
actions.move_to_element(공사버튼).click().perform()

공고기관버튼 = wait.until(EC.element_to_be_clickable((By.ID, 'mf_wfm_container_tacBidPbancLst_contents_tab2_body_untyGrpGb1_input_0')))
actions.move_to_element(공고기관버튼).click().perform()

기관명입력필드 = wait.until(EC.element_to_be_clickable((By.ID, 'mf_wfm_container_tacBidPbancLst_contents_tab2_body_ibxDmstNm1')))
actions.move_to_element(기관명입력필드).click().perform()
기관명입력필드.send_keys('과학기술정보통신부')

참가제한지역 = wait.until(EC.element_to_be_clickable((By.ID, 'mf_wfm_container_tacBidPbancLst_contents_tab2_body_sbxOdnLmtLgdngCd')))
참가제한지역선택 = Select(참가제한지역)
참가제한지역선택.select_by_visible_text('서울특별시')

검색버튼 = wait.until(EC.element_to_be_clickable((By.ID, 'mf_wfm_container_tacBidPbancLst_contents_tab2_body_btnS0004')))
actions.move_to_element(검색버튼).click().perform()

상세조건버튼.click()

입찰공고목록결과 = wait.until(EC.element_to_be_clickable((By.ID, 'mf_wfm_container_tacBidPbancLst_contents_tab2_body_wq_uuid_2256')))
입찰공고목록리스트 = 입찰공고목록결과.find_elements(By.CSS_SELECTOR, 'table#mf_wfm_container_tacBidPbancLst_contents_tab2_body_gridView1_body_table tbody tr')
print(len(입찰공고목록리스트))

for 입찰공고 in 입찰공고목록리스트:
    공고명요소 = 입찰공고.find_element(By.CSS_SELECTOR, 'td:nth-of-type(7)')
    공고명 = 공고명요소.text
    if(공고명):
        print(공고명)

driver.close()
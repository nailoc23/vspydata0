import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By # 4버전 이후 태그정보
#from selenium.webdriver.common.keys import Keys
import time # 디버깅 -> 실제는 wait 함수
import random # 일시정지시간을 랜덤하게 변경
from bs4 import BeautifulSoup
sleep_time = random.uniform(0.5, 2.0) # 0.5 ~ 2.0 사이에 랜덤값 (예)0,5555445

driver = webdriver.Chrome()
URL = 'https://www.starbucks.co.kr/index.do'
driver.get(URL)

time.sleep(1)
gnb_store = driver.find_element(By.CSS_SELECTOR, '.gnb_nav03 a')
gnb_store.click()

time.sleep(1)
store_btn = driver.find_element(By.CSS_SELECTOR, 'div.store_bn1_btn>a')
store_btn.click()

#페이지 이동됨

time.sleep(1)
local_taB = driver.find_element(By.CSS_SELECTOR, 'header.loca_search a')
local_taB.click() #지역검색

time.sleep(1)
sidoes = driver.find_element(By.CLASS_NAME, 'sido_arae_box')
seoul_li = sidoes.find_elements(By.TAG_NAME, 'li')
seoul_li[0].click() # 시도 (서울)

time.sleep(10)
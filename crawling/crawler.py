# 웹 크롤링 (Crawling) : 브라우저 드라이버를 이용하여 실제로 각 페이지를 이동하며 '동적'으로 데이터를 수집하는 방법

# 웹 스크래핑(Scrapping) : 웹 페이지의 응답을 받아 데이터를 분석하여  필요한 데이터를 수집하는 방법

# 파이썬 스크랩핑 패키지: beautifulsoup4
# 파이썬 크롤링 패키지: selenium

# pip install beatifulsoup4
# pip install selenium
# pip install beatifulsoup4 selenium

#pip install requests

# 100 추가 요청 기다림
# 200 성공
# 300 리소스 위치가 올바르지 않다?
# 400 요청자 클라이언트 오류
# 500 응답자 서버 오류

import requests # 요청
from bs4 import BeautifulSoup # 요청해줘잉

URL = 'http://naver.com' # 얘한테 요청

response = requests.get(URL)
# print(response.status_code) 상태 코드
# print(response.text) 뭘 다 받아옴 먼지 나도 몰루

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html,'html.parser')
    a_list = soup.find_all('a') # a라는 태그만 html에서 찾는거~
    # print(a_list)

else:
    print(response.status_code)

from selenium import webdriver
from selenium.webdriver import ActionChains # 클릭관련 머시기
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
import time

driver = webdriver.Chrome()
time.sleep(2)

driver.get(URL)
time.sleep(2)

# 크롬이 켜져서 1초뒤 제네시스를 입력함
search_input = driver.find_element(By.ID,'query')
search_input.send_keys('제네시스') 
time.sleep(1)

search_input.send_keys(Keys.ENTER) # 크롬이 켜진 뒤 1초뒤 제네시스를 입력하고 엔터
time.sleep(2)

news_button = driver.find_element(By.CSS_SELECTOR, '#lnb > div.lnb_group > div > div.lnb_nav_area._nav_area_root > div > div.api_flicking_wrap._conveyer_root > div:nth-child(8) > a') # 3초 뒤
time.sleep(1)

ActionChains(driver).click(news_button).perform()
time.sleep(2)

# 클래스로 검색할적에는 find_elements을 사용
news_title_elements = driver.find_elements(By.CLASS_NAME, 'news_tit')
time.sleep(1)

for news_title_element in news_title_elements:
    # title = news_title_element.text
    title =news_title_element.get_attribute('title')
    print(title)
time.sleep(1)

driver.back() # 뒤로감
time.sleep(2)

image_button = driver.find_element(By.CSS_SELECTOR, '#lnb > div.lnb_group > div > div.lnb_nav_area._nav_area_root > div > div.api_flicking_wrap._conveyer_root > div:nth-child(1) > a') 
time.sleep(1)

ActionChains(driver).click(image_button).perform()
time.sleep(2)

images_elements = driver.find_elements(By.CLASS_NAME, '_fe_image_tab_content_thumbnail_image')
time.sleep(1)

image_list = []

for images_element in images_elements:
    image_src = images_element.get_attribute('src')
    image_list.append(image_src)
    print(image_src)
time.sleep(1)

# 파이썬으로 폴더 생성
import os

FOLDER_PATH = r'./images/'

if not os.path.isdir(FOLDER_PATH):
    os.mkdir(FOLDER_PATH)
# 파이썬으로 폴더 생성//

# 파이썬으로 이미지 url 파일 다운로드   
from urllib.request import urlretrieve

number = 1

for image_src in image_list:
    urlretrieve(image_src, FOLDER_PATH + f'{number}.png')
    number += 1
    time.sleep(0.5)
# 파이썬으로 이미지 url 파일 다운로드//
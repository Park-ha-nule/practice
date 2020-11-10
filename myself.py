from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime
import threading

end = False

# chromedriver 가 설치되어 있는 경로 입력
driver = webdriver.Chrome('C:/Program Files (x86)/Chrome/chromedriver.exe')
# 웹 자원 로드를 위해 3초 대기
driver.implicitly_wait(3)
# 네이버 실시간 검색어 크롤링을 하기위해 실시간 검색어가 있는 웹 사이트를 불러온다.
driver.get('https://datalab.naver.com/keyword/realtimeList.naver?where=main')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

content = soup.find_all('div', {'class' : 'selection_area'})
print(content.text)

def crawling(second = 1.0):
    global end
    if end:
        return
    # '실시간검색어.txt' 가 다른 블로그에서는 실시간급상승.md로 되어있는 곳도 있는데 둘 중 어느것을 하든 상관없다.
    # content = soup.find_all('div', {'class' : 'selection_area'})
    # print(content.text)
    li = soup.find('li', {'class' : 'realtime_item connect_on keyword_on'})
    a = li.find_all('a')
    print(li)
    print(a)
    # <li class = "realtime_item connect_on keyword_on" data-rtk-rank="1">
    # <a href="">
    # <strong class="rank">
    # <span class="bind">위
    # <span clas="keyword">박지선 유서


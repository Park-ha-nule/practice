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

def crawling(second = 1.0):
    global end
    if end:
        return
    # '실시간검색어.txt' 가 다른 블로그에서는 실시간급상승.md로 되어있는 곳도 있는데 둘 중 어느것을 하든 상관없다.
    f = open('실시간검색어.txt', 'a')
    f.write(datetime.today().strftime('\n'+"_______________"+'\n'+"%Y/%m/%d %H:%M:%S") + '\n')
    i = 1
    for anchor in soup.select("span.item_title"):
        data = str(i) + "위: " + anchor.get_text() + '\n'
        f.write(data)
        i += 1
        print(data)
    f.close()
    f = open('연령.txt', 'w')
    f.write(datetime.today().strftime('\n' + "_______________" + '\n' + "%Y/%m/%d %H:%M:%S") + '\n')
    age_filter = soup.find('div', {'class' : 'graph_tab_box'})
    age = age_filter.find('li', {'class' : 'on'})
    real_age = age.text
    if '전체' in real_age:
        print("전체 연령")
    else:
        print("10대 20대 30대 등등")

    f.close()
    threading.Timer(second, crawling, [second]).start()

crawling(900)
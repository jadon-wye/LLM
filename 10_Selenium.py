# 네이버 웹툰 댓글 크롤링
# https://comic.naver.com/webtoon/detail?titleId=834886&no=53&week=mon
import time
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get('https://comic.naver.com/webtoon/detail?titleId=834886&no=53&week=mon')
soup = BeautifulSoup(driver.page_source) # request.text와 같음 -> html 코드를 가져옴
comment_area = soup.find_all('span', {'class': 'u_cbox_contents'})
print('*********** 베스트 댓글 **********')
for i in range(len(comment_area)):
    comment = comment_area[i].text.strip()
    print(comment)
    print('-' * 30)

# /html/body/div[1]/div[5]/div/div/div[4]/div[1]/div[3]/div/div/div[4]/div[1]/div/ul/li[2]/a/span[2]
driver.find_element('xpath', '/html/body/div[1]/div[5]/div/div/div[4]/div[1]/div[3]/div/div/div[4]/div[1]/div/ul/li[2]/a/span[2]').click()

time.sleep(2) # 클릭으로 웹페이지가 전환하는 속도보다 for문이 도는 속도가 더 빨라서 2초정도 웹페이지 로딩할 시간을 줌

soup = BeautifulSoup(driver.page_source)
comment_area = soup.find_all('span', {'class': 'u_cbox_contents'})
print('*********** 전체 댓글 **********')
for i in range(len(comment_area)):
    comment = comment_area[i].text.strip()
    print(comment)
    print('-' * 30)


time.sleep(30)
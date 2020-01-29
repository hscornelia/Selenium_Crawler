from Connect import *
from bs4 import BeautifulSoup

class Parsing:

    # 맛집 리스트 URL 수집
    def getLink(self):
        html_doc = driver.page_source
        soup = BeautifulSoup(html_doc, 'html.parser')
        links = []

        # list들 중에서 a 태그를 찾아야 함.
        for link in soup.find_all('div', {'class': 'info'}):
            ref = link.find('a', href=True)
            links.append(ref.get('href'))
        print(links)

        # 각각의 링크들 순회하면서 정보 받아오기
        return links

    # 맛집 리스트 내용 수집
    def getData(self):
        html_doc = driver.page_source
        soup = BeautifulSoup(html_doc, 'html.parser')

        # title 
        title = soup.find('h1', {'class': 'restaurant_name'}, text=True).text
        point = soup.find('strong', {'class': 'rate-point'}).find('span', text=True).text
        addr = soup.find('span', {'class': 'Restaurant__InfoAddress--Text'}).text

        print(title)
        print(point)
        print(addr)




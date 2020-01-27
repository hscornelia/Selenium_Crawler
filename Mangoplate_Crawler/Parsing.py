from Connect import *
from bs4 import BeautifulSoup

class Parsing:

    # 맛집 리스트 URL 수집
    def getLink(self):
        html_doc = driver.page_source
        soup = BeautifulSoup(html_doc, 'html.parser')
        links = []
        for link in soup.find_all('a', {'class': 'only-desktop_not'}):
            print(link.get('ng-href'))


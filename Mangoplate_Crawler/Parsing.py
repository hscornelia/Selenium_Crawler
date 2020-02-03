from Connect import *
from ConnectDB import *
from bs4 import BeautifulSoup

class Parsing:

    def getPage(self):
        html_doc = driver.page_source
        soup = BeautifulSoup(html_doc, 'html.parser')
        pages = []

        for i in soup.find('p', {'class': 'paging'}).find_all('a'):
            page = i.text.strip() 
            pages.append(page)   
        max_page = max(page)
        
        return int(max_page)



    # 맛집 리스트 URL 수집
    def getLink(self):
        html_doc = driver.page_source
        soup = BeautifulSoup(html_doc, 'html.parser')
        links = []

        # list들 중에서 a 태그를 찾아야 함.
        for link in soup.find_all('div', {'class': 'info'}):
            ref = link.find('a', href=True)
            links.append(ref.get('href'))
            #print(links)

        # 각각의 링크들 순회하면서 정보 받아오기
        #print(links)
        return links

    # 맛집 리스트 내용 수집
    def getData(self):
        html_doc = driver.page_source
        soup = BeautifulSoup(html_doc, 'html.parser')

        # Default Values
        title = ''
        point = '0'
        addr = ''
        phone = ''
        category = ''
        price_range = ''
        parking = False
        time = ''

        # title 
        title = soup.find('h1', {'class': 'restaurant_name'}, text=True).text
        if soup.find('strong', {'class': 'rate-point'}) is not None:
            point = soup.find('strong', {'class': 'rate-point'}).find('span', text=True).text
        addr = soup.find('span', {'class': 'Restaurant__InfoAddress--Text'}).text
        tables = soup.findAll('tr')

        # table 안에 labled 되지 않은 여러 내용들이 들어가 있어서 일일히 필터링 해주어야 함

        for row in tables:
            temp = row.find('th').text.strip()
            if(temp == '전화번호'):
                phone = row.find('td').text.strip()
            if(temp == '음식 종류'):
                category = row.find('td').text.strip()
            if(temp == '가격대'):
                price_range = row.find('td').text.strip()
            if(temp == '주차'):
                park_temp = row.find('td').text.strip() 
                if(park_temp == '주차공간없음'):
                    parking = False
                if (park_temp == '무료주차 가능'):
                    parking = True
            if(temp == '영업시간'):
                time = row.find('td').text.strip()



        connect = ConnectDB()
        restaurantInfo = {
            'name': title,
            'point': point,
            'address': addr,
            'business_hour': time,
            'pricerange': price_range,
            'category': category,
            'parking_space': parking,
            'location': '',
        }
        connect.addRestaurant(restaurantInfo)

        #print(title)
        #print(point)
        #print(addr)
        #print(phone)
        #print(category)
        #print(price_range)
        #print(parking)
        #print(time)




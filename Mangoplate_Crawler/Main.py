from Connect import *
from Parsing import *

if __name__ == '__main__' :
    
    parser = Parsing()

    # 서울대입구
    print('서울대 입구 주소')
    connectPage('서울대입구')
    #max_page = parser.getPage()
    max_page = 2
    for i in range(1, max_page):
        connectSearch('서울대입구', i)
        links = parser.getLink()
        
        for link in links:
            connectDetail(link)
            parser.getData()

    # 낙성대
    print('낙성대역 주소')
    connectPage('낙성대')
    #max_page = parser.getPage()
    max_page = 2
    for i in range(1, max_page):
        connectSearch('낙성대', i)
        links = parser.getLink()

        for link in links:
            connectDetail(link)
            parser.getData()

    #신림
    print('신림역 주소')
    connectPage('신림')
    #max_page = parser.getPage()
    max_page = 2
    for i in range(1, max_page):
        connectSearch('신림', i)
        links = parser.getLink()

        for link in links:
            connectDetail(link)
            parser.getData()
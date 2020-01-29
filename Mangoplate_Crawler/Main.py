from Connect import *
from ElementControl import *
from Parsing import *

if __name__ == '__main__' :
    
    # 맛집 리스트
    snuUrls = []
    nkdUrls = []

    elem = Element()
    parser = Parsing()

    # 서울대입구
    print('서울대 입구 주소')
    for i in range(1, 10):
        elem.searchPage('서울대입구', i)
        links = parser.getLink()
        
        for link in links:
            elem.searchDetail(link)
            
    # 낙성대
    # print('낙성대역 주소')
    # for i in range(1, 4):
    #     elem.searchPage('낙성대', i)
    #     parser.getLink()

    #신림
    # print('신림역 주소')
    # for i in range(1,10) :
    #     elem.searchPage('신림', i)
    #     parser.getLink()
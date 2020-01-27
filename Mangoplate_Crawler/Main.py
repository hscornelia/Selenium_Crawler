from Connect import *
from ElementControl import *
from Parsing import *

if __name__ == '__main__' :
    
    # 맛집 리스트
    snuUrls = []
    nkdUrls = []

    snu = SNU()
    parser = Parsing()

    parser.getLink()


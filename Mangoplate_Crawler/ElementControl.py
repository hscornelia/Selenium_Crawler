from Connect import *
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys

class Element:
    def __init__(self):
        pass

    def searchPage(self, location, page):
        connectSearch(location, page)

    def searchDetail(self, url):
        connectDetail(url)
from Connect import *
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys

class SNU:
    def __init__(self):
        connect('서울대입구')

class NSD:
    def __init__(self):
        connect('낙성대')

from selenium import webdriver

# ChromeDriver
driver = webdriver.Chrome('/Users/sangchulkim/Downloads/chromedriver')
driver.implicitly_wait(3)

# Function Definition
def initPage():
    driver.get('https://www.mangoplate.com/')

def connectSearch(url, page):
    driver.get('https://www.mangoplate.com/search/' + url + '?keyword=' + url + '&page=' + str(page))

def connectDetail(url):
    driver.get('https://www.mangoplate.com/'+url)
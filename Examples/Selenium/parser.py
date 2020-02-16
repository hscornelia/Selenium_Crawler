from selenium import webdriver

driver = webdriver.Chrome('/Users/sangchulkim/Downloads/chromedriver')
driver.implicitly_wait(3)

driver.get('https://google.com')
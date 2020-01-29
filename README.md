# Selenium_Crawler

Make Crawlers in Python using selenium library
> including Mangoplate_Crawler, Requests_BeautfulSoup, Selenium

## Mangoplate_Crawler

### Dependencies

> - python3
> - selenium 
> - BeautifulSoup

> - install chrome driver
> https://chromedriver.chromium.org/downloads

### Process

1. Main.py executed
2. Element, Parsing Object initialize
3. Search page for specific loactions(e.g 서울대입구), page number should be replaced to other variables
4. Element(location) connects search urls (open page)
5. parser get hashed links of the specific restaurants addresses. (e.g /restaurants/3RGlw_Hr) & stores in the array

--------------------> implemented so far

6. chrome driver accesses each specific page and collects the restaurant data
7. connects to database and stores it.
8. make db_backup file and add it to the Restaurants_api




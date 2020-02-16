# Crawlers

Make Crawlers in Python using selenium library
> including Mangoplate_Crawler, Requests_BeautfulSoup, Selenium

## Mangoplate_Crawler

### Dependencies

> - python3
> - selenium 
> - BeautifulSoup
> - psycopg2

> - install chrome driver
> https://chromedriver.chromium.org/downloads

### Tables

restaurants

| field | type |
| ----- | ---- |
| name | string |
| address | string |
| business_hour | string |
| parking_space | boolean |
| location | string |
| pricerange | string |
| category | string |
| point | string |
| created_at | timestamp(6) |
| updated_at | timesatmp(6) |

### Need to do

1. class 구조화
2. DB 쿼리 최적화
3. Crontab 이용해서 자동으로 실행되도록


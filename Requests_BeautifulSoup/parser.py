# parser.py
import requests
from bs4 import BeautifulSoup

# HTTP GET Request
req = requests.get('https://m.sports.naver.com/news.nhn?oid=076&aid=0003523766')

# GET HTML Source
html = req.text
# header = req.headers
# status = req.status_code
# is_ok = req.ok
soup = BeautifulSoup(html, 'html.parser')

# using CSS Selector
titles = soup.select(
    'span.article_tit'
)

print(titles)
for title in titles:
    print(title.text)
    print(title.get('href'))

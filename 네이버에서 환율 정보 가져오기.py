import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/marketindex"
market_index = requests.get(url)
print(market_index.status_code)

soup = BeautifulSoup(market_index.content, "html.parser")
# class 속성의 값이 div인 태그 아래에서 span 태그가 class 속성의 값이 value인 요소
price = soup.select_one("a.head.jpy_usd div.head_info > span.value")
print(price)
print(price.text)
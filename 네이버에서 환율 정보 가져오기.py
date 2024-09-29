import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/marketindex/' # 환율 정보를 제공하는 URL
market_index = requests.get(url)

print(market_index)

soup = BeautifulSoup(market_index.content, "html.parser")

price = soup.select_one("div.head_info > span.value")
print(price)

print("usd/krw=", price.text)

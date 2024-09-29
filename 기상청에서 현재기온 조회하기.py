import requests
response = requests.get('https://www.weather.go.kr/w/index.do')
print(response.status_code)
print(len(response.text))

from bs4 import BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')
print(soup.select('.tmp'))

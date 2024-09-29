import requests

# response = requests.get('https://jsonplaceholder.typicode.com/posts')
# print(response.status_code)  # HTTP 상태 코드 출력
# print(response.text)         # 응답 본문 출력
# print(response.json())       # JSON 응답을 파싱하여 출력

import os
absolute_path = os.path.abspath("sample.html")
drive, path = os.path.splitdrive(absolute_path)

import requests
from requests_file import FileAdapter
s = requests.Session()
s.mount('file://', FileAdapter())
res = s.get("file://"+path.replace('\\', '/'))
res.encoding = 'utf-8'
print(res.text)

from bs4 import BeautifulSoup
soup = BeautifulSoup(res.content, 'html.parser')
print(soup)

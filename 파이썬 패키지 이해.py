import requests

# response = requests.get("https://jsonplaceholder.typicode.com/posts")
#
# print(response.status_code)
# print(response.text)
# print(response.json())

import os
absolute_path = os.path.abspath("sample.html")
print(absolute_path)

drive, path = os.path.splitdrive(absolute_path)
print(drive, path)

from requests_file import FileAdapter
s = requests.Session()
s.mount("file://", FileAdapter())
res = s.get("file://" + path.replace("\\", "/"))
res.encoding = 'utf-8'
# print(res.text)
# print(res.content)
from bs4 import BeautifulSoup
soup = BeautifulSoup(res.content, 'html.parser') # HTML문서의 내용을 파싱합니다.
# print(soup) # 솝 객체를 출력하면 HTML 문서의 모든 내용이 출력됩니다.
print(soup.select_one("h1").text)
print(soup.select("h1")[0].text)
elements = soup.select("h1")
for element in elements:
    print(element.text)
print(soup.select_one("div b")) # 자손 선택자, 내포 선택자
print(soup.select_one("div > b")) # 자식 선택자
print(soup.select_one("#subject"))
print(soup.select_one("#subject").text)
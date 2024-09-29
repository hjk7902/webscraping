# 도서 정보를 저장할 클래스 선언합니다.
class Book:
    def __init__(self, rank, title, author, price):
        self.rank = rank
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"{self.rank}, {self.title}, {self.author}, {self.price}"

    def to_dict(self):
        return {'rank':self.rank, 'title':self.title,
                'author':self.author, 'price':self.price}


import requests
from bs4 import BeautifulSoup

url = 'https://www.yes24.com/Product/Category/BestSeller?categoryNumber=001'
bestseller = requests.get(url)
soup = BeautifulSoup(bestseller.content, "html.parser")

best_list_el = soup.select("#yesBestList div.item_info")
print(len(best_list_el))

# 도서 목록을 저장할 리스트를 선언
book_list = []

# 각 리스트에 요소를 찾아서 추가(append)
for i, item in enumerate(best_list_el):
    title = item.select_one("div.info_name > a").text
    author = item.select_one(".info_auth > a").text
    price = item.select_one(".info_price .txt_num").text
    book_list.append(Book(i+1, title, author, price))

# 화면에 출력하기
for book in book_list:
    print(book)
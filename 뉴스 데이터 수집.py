import requests
from bs4 import BeautifulSoup

jtbc_economy = requests.get("https://fs.jtbc.co.kr/RSS/economy.xml")
economy_news_soup = BeautifulSoup(jtbc_economy.content, "xml")

link_list = economy_news_soup.select("item > link")
print(len(link_list))
print(link_list[0].text)

news_data = []
for link in link_list:
    news = requests.get(link.text)
    news_soup = BeautifulSoup(news.content, "html.parser")
    news_content = news_soup.select_one("#articlebody > .article_content")
    news_data.append(news_content.text)


import pandas as pd
news_df = pd.DataFrame(data=news_data, columns=["news"])
print(news_df.head())
news_df.to_csv("news.txt", encoding="utf-8-sig", index=False)
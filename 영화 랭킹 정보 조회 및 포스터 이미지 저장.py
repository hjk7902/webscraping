import requests
from bs4 import BeautifulSoup
from io import BytesIO
from PIL import Image
import re
import os

url = "https://www.moviechart.co.kr/rank/realtime/index/image"
movie_ranking = requests.get(url)

image_dir = 'images'
if not os.path.exists(image_dir):
  os.makedirs(image_dir)

pattern = r'[\\/:"*?<>|]'

if movie_ranking.status_code == 200:
  print("영화 정보를 출력합니다.")
  soup = BeautifulSoup(movie_ranking.content, 'html.parser')
  movie_list = soup.select(".movieBox-list .movie-title a")
  movie_image_list = soup.select(".movieBox-list .movieBox-item img")
  print(f"수집한 영화 수: {len(movie_list)}")
  for movie, movie_image in zip(movie_list, movie_image_list):
    image_src = movie_image.get('src')
    image_response = requests.get("https://www.moviechart.co.kr" +
                                  image_src)
    img = Image.open(BytesIO(image_response.content))
    image_filename = re.sub(pattern, '', movie.text)
    img.save(os.path.join(image_dir, image_filename + ".png"))
    print(movie.text, )
else:
  print("페이지에 연결할 수 없습니다.")
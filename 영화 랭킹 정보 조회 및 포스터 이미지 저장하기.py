import requests
from bs4 import BeautifulSoup
from io import BytesIO
from PIL import Image
import re
import os
from urllib.parse import urlparse, parse_qs

movie_ranking = requests.get('https://www.moviechart.co.kr/rank/realtime/index/image')

image_dir = 'images'
if not os.path.exists(image_dir):
    os.makedirs(image_dir)

print(movie_ranking.status_code)
pattern = re.compile(r'[\\/:"*?<>|]') # 파일명에 넣을 수 없는 특수문자들
if movie_ranking.status_code==200:
    soup = BeautifulSoup(movie_ranking.content, 'html.parser')
    movie_list = soup.select('.movieBox-list .movie-title a')
    movie_image_list = soup.select('.movieBox-list .movieBox-item img')
    print(len(movie_list), len(movie_image_list))
    for movie_title, movie_image in zip(movie_list, movie_image_list):
        print(movie_title.text)
        url = movie_image.get('src')
        # print(image_src)
        # /thumb?width=178&height=267&m_code=20224666&source=https://www.moviechart.co.kr/assets/upload/movie/240712102511_7239.jpg
        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)
        image_src = query_params.get('source', [None])[0]
        # image_response = requests.get('https://www.moviechart.co.kr' + image_src)
        image_response = requests.get(image_src)
        img = Image.open(BytesIO(image_response.content))
        image_filename = pattern.sub('', movie_title.text)
        img.save(os.path.join(image_dir, image_filename+'.png'))
else:
    print('페이지를 열 수 없습니다.')
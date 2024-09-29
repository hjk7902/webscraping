html = """
<html>
<head><title>HTML Sample</title>
</head>
<body>
    <h1>Hello CSS</h1>
    <div id="subject">선택자</div>
    <div class="contents">선택자를 어떻게 작성하느냐에 따라
      <span>다른 <b>요소가 반환</b></span> 됩니다.</div>
    <div>CSS 선택자는 다양한 곳에서 <b>활용</b>됩니다.</div>
</body>
</html>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

print(soup)

el = soup.select_one("h1")
print(el)
print(el.text)

div_el = soup.select("div")
print(div_el)

print(soup.select_one("div"))

print(soup.select("h1, span"))

print(soup.select("div b"))

print(soup.select("div > b"))

print(soup.select("div b"))

print(soup.select(".contents"))

print(soup.select("#subject"))

print(soup.select("[id=subject]"))
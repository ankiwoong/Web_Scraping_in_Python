from bs4 import BeautifulSoup
from urllib.request import urlopen

# urllib.properties 모듈의 urlopenhroperties를 사용하여 URL http://olympus.realpython.org/profiles/dionysus 열기
url = "http://olympus.realpython.org/profiles/dionysus"

page = urlopen(url)

# 페이지에서 HTML을 문자열로 읽고 html 변수에 할당
html = page.read().decode("utf-8")

# BeautifulSoup 객체를 작성하여 soup 변수에 할당
soup = BeautifulSoup(html, "html.parser")

print(soup)

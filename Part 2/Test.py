#  urlib.request 모듈에서 urlopen 기능을 가져오고 bs4 패키지에서 BeautifulSoup 클래스를 가져오십시오.
from urllib.request import urlopen
from bs4 import BeautifulSoup

# /profiles 페이지의 각 링크 URL은 상대 URL이므로 웹사이트의 기본 URL로 base_url 변수를 생성하십시오.
base_url = "http://olympus.realpython.org"

# 이제 urlopen()이 있는 /profiles 페이지를 열고 .read()를 사용하여 HTML 소스를 가져오십시오.
html_page = urlopen(base_url + "/profiles")
html_text = html_page.read().decode("utf-8")

# 다운로드 및 디코딩된 HTML 소스로 새 BeautifulSoup 개체를 생성하여 HTML 구문 분석
soup = BeautifulSoup(html_text, "html.parser")

# suff.find_all("a")은 HTML 소스의 모든 링크 목록을 반환한다. 이 목록을 반복하여 웹 페이지의 모든 링크를 출력 할 수 있다.
for link in soup.find_all("a"):
    link_url = base_url + link["href"]
    print(link_url)

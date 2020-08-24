from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"

page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

# 출력
print(soup.get_text())

# find_all()을 사용하여 특정 태그의 모든 인스턴스 목록을 반환할 수 있다.
find_all_ex1 = soup.find_all("img")

# 출력
print(find_all_ex1)

# 각 Tag 개체는 HTML 태그 유형을 포함하는 문자열을 반환하는 .name 속성을 가지고 있다.
# 태그 객체의 HTML 속성에 액세스할 수 있다.
image1, image2 = soup.find_all("img")
find_name_ex1 = image1.name
find_name_ex2 = image2.name

# 출력
print(find_name_ex1)
print(find_name_ex2)

# Dionysus 프로필 페이지에서 이미지의 소스를 가져오려면 딕셔너리를 사용하여 src 속성에 액세스하십시오.
img_dic_1 = image1["src"]
img_dic_2 = image2["src"]

# 출력
print(img_dic_1)
print(img_dic_2)

# HTML 문서의 특정 태그는 태그 개체의 속성으로 액세스할 수 있다.
# 예를 들어, 문서에서 태그를 가져오려면 .title 속성을 사용하십시오.
title = soup.title

# 출력
print(title)

# Tag 객체의 .string 속성이 있는 제목 태그 사이의 문자열만 검색할 수도 있다.
title_string = soup.title.string

# 출력
print(title_string)

# 값 /static/dionysus.jpg와 동일한 src 속성을 가진 모든 태그를 찾으려면 .find_all()에 다음과 같은 추가 인수를 제공하면 된다.
find_all_ex2 = soup.find_all("img", src="/static/dionysus.jpg")

# 출력
print(find_all_ex2)

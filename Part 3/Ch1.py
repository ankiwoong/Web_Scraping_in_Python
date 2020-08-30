import mechanicalsoup

browser = mechanicalsoup.Browser()

# browser() 객체는 head가 없는 웹 브라우저를 나타낸다.
# URL을 .get() 메소드에 전달하여 인터넷에서 페이지를 요청할 수 있다.
url = "http://olympus.realpython.org/login"
page = browser.get(url)

# 출력
print(page)

# MechanicalSoup은 요청에서 HTML을 구문 분석하기 위해 Beautiful Soup을 사용한다.
# 페이지에는 BeautifulSoup 개체를 나타내는 .soup 속성이 있다
print(type(page.soup))

# .soup 속성을 검사하여 HTML을 볼 수 있다.
print(page.soup)

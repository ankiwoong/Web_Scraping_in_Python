from urllib.request import urlopen

# 대상 url 지정
url = "http://olympus.realpython.org/profiles/aphrodite"

# URL을 urlopen()으로 전달
page = urlopen(url)

# 결과물 출력
print(page)

# 페이지에서 HTML을 추출하려면 먼저 바이트 시퀀스를 반환하는 HTTPRespontse 개체의 .read() 메서드를 사용
html_bytes = page.read()

# decode()를 사용하여 UTF-8을 사용하여 바이트를 문자열로 디코딩
html = html_bytes.decode("utf-8")

# 결과물 출력
print(html)

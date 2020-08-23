from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/aphrodite"
page = urlopen(url)

html_bytes = page.read()
html = html_bytes.decode("utf-8")

# .find()는 하위 문자열의 첫 번째를 반환하므로 .find()에 문자열 "<title>"을 전달하면 태그의 인덱스를 얻을 수 있다.
title_index = html.find("<title>")

# 출력
print(title_index)

# 제목에 있는 첫 번째 문자의 색인을 가져오려면 "<title>" 문자열의 길이를 title_index에 추가할 수 있습니다.
start_index = title_index + len("<title>")

# 출력
print(start_index)

# 문자열 "<title>" 태그의 색인을 구하십시오.
end_index = html.find("</title>")

# 출력
print(end_index)

# 마지막으로 html 문자열을 자르면 제목을 추출할 수 있다.
title = html[start_index:end_index]

# 출력
print(title)

# 대상 url 재지정
url = "http://olympus.realpython.org/profiles/poseidon"

# 예제와 동일한 방법으로 이 새 URL에서 제목을 추출
page = urlopen(url)
html = page.read().decode("utf-8")
start_index = html.find("<title>") + len("<title>")
end_index = html.find("</title>")
title = html[start_index:end_index]

# 출력
print(title)

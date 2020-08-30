import mechanicalsoup

"""
HTML 코드의 중요한 섹션은 로그인 양식, 즉 태그 안의 모든 것이다.
이 페이지의 에는 로그인하도록 설정된 이름 속성이 있다.
이 양식은 두 개의 요소를 포함하고 있는데, 하나는 지명된 사용자, 다른 하나는 지명된 pwd이다.
세 번째 요소는 제출 버튼이다
"""

# 브라우저 인스턴스를 생성하고 이를 사용하여 URL http://olympus.realpython.org/login을 요청하십시오.
# .soup 속성을 사용하여 페이지의 HTML 내용을 login_html 변수에 할당하십시오.
browser = mechanicalsoup.Browser()
url = "http://olympus.realpython.org/login"
login_page = browser.get(url)
login_html = login_page.soup

# login_reason.selectegramform")은 페이지에 있는 모든 요소의 목록을 반환한다.
# 페이지에는 요소가 하나만 있으므로 리스트의 색인 0에서 요소를 검색하면 양식에 접근할 수 있다.
# 다음 두 줄은 사용자 이름과 비밀번호 입력을 선택하고 값을 각각 "zeus"와 "ThunderDude"로 설정한다.
form = login_html.select("form")[0]
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

# login_page.url을 통해 액세스하는 login_page의 URL과 같은 두 가지 인수를 이 메서드에 전달한다는 점에 유의하십시오.
profiles_page = browser.submit(form, login_page.url)

# 출력
print(profiles_page.url)

# .select()를 다시 사용하여 이번에는 문자열 "a"를 전달하여 페이지의 모든 앵커 요소를 선택하십시오.
links = profiles_page.soup.select("a")

# 각 링크에 반복해서 href 속성을 출력할 수 있다.
for link in links:
    address = link["href"]
    text = link.text

    print(f"{text}: {address}")

# 이 경우 기본 URL은 http://olympus.realpython.org일 뿐이다.
# 그런 다음 src 속성에 있는 상대 URL과 기본 URL을 연결하십시오.
base_url = "http://olympus.realpython.org"

for link in links:
    address = base_url + link["href"]
    text = link.text

    print(f"{text}: {address}")

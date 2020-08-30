# 먼저 mechanicalsoup 패키지를 가져와 Broswer 개체를 생성하십시오.
import mechanicalsoup

browser = mechanicalsoup.Browser()

# URL을 browser.get()에 전달하여 브라우저를 로그인 페이지로 가리키고 .soup 속성이 있는 HTML을 가져오십시오.
login_url = "http://olympus.realpython.org/login"
login_page = browser.get(login_url)
login_html = login_page.soup

# login_html은 BeautifulSoup 인스턴스다. 페이지에는 하나의 양식만 있으므로 login_html.form을 통해 양식에 접근할 수 있다.
# .select()를 사용하여 사용자 이름과 암호 입력을 선택하고 사용자 이름 "zeus"와 암호 "ThunderDude"로 입력하십시오.
form = login_html.form
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

# 이제 양식이 작성되었으니 브라우저로 제출하면 된다.
profiles_page = browser.submit(form, login_page.url)

# 출력
print(profiles_page.soup.title)

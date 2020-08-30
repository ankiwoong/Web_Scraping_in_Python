### <p>웹 스크래핑은 웹에서 원시 데이터를 수집하고 분석하는 과정입니다. Python커뮤니티는 매우 강력한 웹 스크래핑 도구를 고안해 냈습니다.</p>

### <p>인터넷은 아마도 지구상에서 가장 큰 정보의 원천이자 정보의 원천인 것 같다. 데이터 과학, 비즈니스 인텔리전스 및 조사 보고 와 같은 많은 분야에서 웹 사이트에서 데이터를 수집하고 분석하면 큰 이점을 얻을 수 있습니다.</p>

### <p>이 자습서에서는 다음과 같은 방법을 배울 수 있습니다.</p>

---

* 문자열 방법 및 정규식을 사용하여 웹 사이트 데이터 구문 분석
HTML구문 분석기를 사용하여 웹 사이트 데이터 구문 분석
양식 및 기타 웹 사이트 구성 요소와 상호 작용

* 웹 사이트에서 텍스트 스크롤 및 구문 분석
  * 자동화된 프로세스를 사용하여 웹 사이트에서 데이터를 수집하는 것을 웹 스크랩이라고 합니다. 일부 웹 사이트에서는 사용자가 본 자습서에서 만들 도구와 같은 자동 도구를 사용하여 데이터를 스크랩하는 것을 명시적으로 금지합니다. 웹 사이트에서는 다음과 같은 두가지 이유로 이를 수행할 수 있는 이유는 다음과 같습니다.

  * 그 사이트는 데이터를 보호해야 할 합당한 이유가 있다. 예를 들어 Google지도는 너무 많은 결과를 너무 빨리 요청하지 않습니다.
  웹 사이트의 서버에 반복적으로 요청을 많이 하면 대역 폭이 사용되고, 다른 사용자를 위해 웹 사이트 속도가 느려지며, 웹 사이트가 완전히 응답하지 않도록 서버에 과부하가 걸릴 수 있습니다.

  * 웹 스크래핑에 Python기술을 사용하기 전에 항상 대상 웹 사이트의 허용 가능한 사용 정책을 확인하여 자동화된 도구로 웹 사이트에 액세스 하는 것이 사용 조건을 위반하는 것인지 확인해야 합니다. 법적으로 웹 사이트의 요구에 반대하는 웹 스크래핑은 매우 애매한 영역이다.

  * 웹 스크래핑을 금지하는 웹 사이트에서 사용하는 경우 다음 기술이 불법일 수 있습니다.

---

* 가상환경 설정

```python
python -m venv venv
```

* requests 설치

```python
pip install requests
```

```console
Collecting requests
  Using cached https://files.pythonhosted.org/packages/45/1e/0c169c6a5381e241ba7404532c16a21d86ab872c9bed8bdcd4c423954103/requests-2.24.0-py2.py3-none-any.whl
Collecting urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 (from requests)
  Using cached https://files.pythonhosted.org/packages/9f/f0/a391d1463ebb1b233795cabfc0ef38d3db4442339de68f847026199e69d7/urllib3-1.25.10-py2.py3-none-any.whl
Collecting chardet<4,>=3.0.2 (from requests)
  Using cached https://files.pythonhosted.org/packages/bc/a9/01ffebfb562e4274b6487b4bb1ddec7ca55ec7510b22e4c51f14098443b8/chardet-3.0.4-py2.py3-none-any.whl
Collecting idna<3,>=2.5 (from requests)
  Using cached https://files.pythonhosted.org/packages/a2/38/928ddce2273eaa564f6f50de919327bf3a00f091b5baba8dfa9460f3a8a8/idna-2.10-py2.py3-none-any.whl
Collecting certifi>=2017.4.17 (from requests)
  Using cached https://files.pythonhosted.org/packages/5e/c4/6c4fe722df5343c33226f0b4e0bb042e4dc13483228b4718baf286f86d87/certifi-2020.6.20-py2.py3-none-any.whl
Installing collected packages: urllib3, chardet, idna, certifi, requests
Successfully installed certifi-2020.6.20 chardet-3.0.4 idna-2.10 requests-2.24.0 urllib3-1.25.10
```

* Beautiful Soup 설치

```python
pip install beautifulsoup4
```

```console
Collecting beautifulsoup4
  Using cached https://files.pythonhosted.org/packages/66/25/ff030e2437265616a1e9b25ccc864e0371a0bc3adb7c5a404fd661c6f4f6/beautifulsoup4-4.9.1-py3-none-any.whl
Collecting soupsieve>1.2 (from beautifulsoup4)
  Using cached https://files.pythonhosted.org/packages/6f/8f/457f4a5390eeae1cc3aeab89deb7724c965be841ffca6cfca9197482e470/soupsieve-2.0.1-py3-none-any.whl
Installing collected packages: soupsieve, beautifulsoup4
Successfully installed beautifulsoup4-4.9.1 soupsieve-2.0.1
```

* MechanicalSoup 설치
  
```python
pip install MechanicalSoup
```

```console
Collecting MechanicalSoup
  Downloading https://files.pythonhosted.org/packages/0b/fe/4f871ec3379080c5979815bfec3266871e555eebf4879f551a7e5dee4766/MechanicalSoup-0.12.0-py2.py3-none-any.whl
Collecting lxml (from MechanicalSoup)
  Using cached https://files.pythonhosted.org/packages/bd/a3/4b377aaf02ea39585b81ad9f630226e296d983e9a94d7b78a4bc5e27226d/lxml-4.5.2-cp37-cp37m-win_amd64.whl
Requirement already satisfied: requests>=2.0 in d:\code\study\web_scraping_in_python\venv\lib\site-packages (from MechanicalSoup) (2.24.0)
Collecting six>=1.4 (from MechanicalSoup)
  Using cached https://files.pythonhosted.org/packages/ee/ff/48bde5c0f013094d729fe4b0316ba2a24774b3ff1c52d924a8a4cb04078a/six-1.15.0-py2.py3-none-any.whl
Requirement already satisfied: beautifulsoup4>=4.4 in d:\code\study\web_scraping_in_python\venv\lib\site-packages (from MechanicalSoup) (4.9.1)
Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in d:\code\study\web_scraping_in_python\venv\lib\site-packages (from requests>=2.0->MechanicalSoup) (1.25.10)
Requirement already satisfied: idna<3,>=2.5 in d:\code\study\web_scraping_in_python\venv\lib\site-packages (from requests>=2.0->MechanicalSoup) (2.10)
Requirement already satisfied: chardet<4,>=3.0.2 in d:\code\study\web_scraping_in_python\venv\lib\site-packages (from requests>=2.0->MechanicalSoup) (3.0.4)
Requirement already satisfied: certifi>=2017.4.17 in d:\code\study\web_scraping_in_python\venv\lib\site-packages (from requests>=2.0->MechanicalSoup) (2020.6.20)
Requirement already satisfied: soupsieve>1.2 in d:\code\study\web_scraping_in_python\venv\lib\site-packages (from beautifulsoup4>=4.4->MechanicalSoup) (2.0.1)
Installing collected packages: lxml, six, MechanicalSoup
Successfully installed MechanicalSoup-0.12.0 lxml-4.5.2 six-1.15.0
```
---

# Part1 웹 사이트에서 텍스트 스크래치 및 구문 분석

<details>
<summary>Ch1 ~ Ch4 + Test Code</summary>
<div markdown="1">
Ch 1> 첫번째 웹 스크래퍼

```python
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/aphrodite"
page = urlopen(url)
print(page)

html_bytes = page.read()
html = html_bytes.decode("utf-8")
print(html)
```

```console
<http.client.HTTPResponse object at 0x000001E62653A668>

<html>

<head>
    <title>Profile: Aphrodite</title>
</head>

<body bgcolor="yellow">
    <center>
        <br><br>
        <img src="/static/aphrodite.gif" />
        <h2>Name: Aphrodite</h2>
        <br><br>
        Favorite animal: Dove
        <br><br>
        Favorite color: Red
        <br><br>
        Hometown: Mount Olympus
    </center>
</body>

</html>
```

---

Ch2> 문자열 메소드를 사용하여 HTML에서 텍스트 추출

```python
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/aphrodite"
page = urlopen(url)

html_bytes = page.read()
html = html_bytes.decode("utf-8")

title_index = html.find("<title>")
print(title_index)

start_index = title_index + len("<title>")
print(start_index)

end_index = html.find("</title>")
print(end_index)

title = html[start_index:end_index]
print(title)

url = "http://olympus.realpython.org/profiles/poseidon"

page = urlopen(url)
html = page.read().decode("utf-8")
start_index = html.find("<title>") + len("<title>")
end_index = html.find("</title>")
title = html[start_index:end_index]

print(title)
```

```console
14
21
39
Profile: Aphrodite

<head>
<title >Profile: Poseidon
```

---

Ch3> 정규 표현식에 대한 우선 순위

```python
import re

find_all_ex1 = re.findall("ab*c", "ac")

print(find_all_ex1)

find_all_ex2 = re.findall("ab*c", "abcd")
find_all_ex3 = re.findall("ab*c", "acc")
find_all_ex4 = re.findall("ab*c", "abcac")
find_all_ex5 = re.findall("ab*c", "abdc")

print(find_all_ex2)
print(find_all_ex3)
print(find_all_ex4)
print(find_all_ex5)

find_all_ex6 = re.findall("ab*c", "ABC")
find_all_ex7 = re.findall("ab*c", "ABC", re.IGNORECASE)

print(find_all_ex6)
print(find_all_ex7)

find_all_ex7 = re.findall("a.c", "abc")
find_all_ex8 = re.findall("a.c", "abbc")
find_all_ex9 = re.findall("a.c", "ac")
find_all_ex10 = re.findall("a.c", "acc")

print(find_all_ex7)
print(find_all_ex8)
print(find_all_ex9)
print(find_all_ex10)

find_all_ex11 = re.findall("a.*c", "abc")
find_all_ex12 = re.findall("a.*c", "abbc")
find_all_ex13 = re.findall("a.*c", "ac")
find_all_ex14 = re.findall("a.*c", "acc")

print(find_all_ex11)
print(find_all_ex12)
print(find_all_ex13)
print(find_all_ex14)

match_results = re.search("ab*c", "ABC", re.IGNORECASE)
match_results_group = match_results.group()

print(match_results_group)

string = "Everything is <replaced> if it's in <tags>."
string = re.sub("<.*>", "ELEPHANTS", string)

print(string)

string2 = "Everything is <replaced> if it's in <tags>."
string2 = re.sub("<.*?>", "ELEPHANTS", string2)

print(string2)
```

```console
['ac']
['abc']
['ac']
['abc', 'ac']
[]
[]
['ABC']
['abc']
[]
[]
['acc']
['abc']
['abbc']
['ac']
['acc']
ABC
Everything is ELEPHANTS.
Everything is ELEPHANTS if it's in ELEPHANTS.
```

---

Ch4> 정규 표현식을 사용하여 HTML에서 텍스트 추출

```python
import re
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")

pattern = "<title.*?>.*?</title.*?>"

match_results = re.search(pattern, html, re.IGNORECASE)

title = match_results.group()
title = re.sub("<.*?>", "", title)

print(title)
```

```console
Profile: Dionysus
```

---
Part 1 테스트>

```python
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"

html_page = urlopen(url)

html_text = html_page.read().decode("utf-8")

for string in ["Name: ", "Favorite Color:"]:
    string_start_idx = html_text.find(string)
   
    text_start_idx = string_start_idx + len(string)

    next_html_tag_offset = html_text[text_start_idx:].find("<")
    text_end_idx = text_start_idx + next_html_tag_offset

    raw_text = html_text[text_start_idx:text_end_idx]

    clean_text = raw_text.strip(" \r\n\t")

    print(clean_text)
```

```console
Dionysus
Wine
```
</div>
</details>

---

# Part2 Python에서 웹 스크래핑에 HTML 파서 사용

<details>
<summary>Ch1 ~ Ch2 + Test Code</summary>
<div markdown="1">

Ch1> BeautifulSoup 객체 작성

```python
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"

page = urlopen(url)

html = page.read().decode("utf-8")

soup = BeautifulSoup(html, "html.parser")

print(soup)
```

```console
<html>
<head>
<title>Profile: Dionysus</title> 
</head>
<body bgcolor="yellow">
<center>
<br/><br/>
<img src="/static/dionysus.jpg"/>
<h2>Name: Dionysus</h2>
<img src="/static/grapes.png"/><br/><br/>
Hometown: Mount Olympus
<br/><br/>
Favorite animal: Leopard <br/>
<br/>
Favorite Color: Wine
</center>
</body>
</html>
```

---

Ch2> BeautifulSoup 객체 사용


```python
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"

page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

print(soup.get_text())

find_all_ex1 = soup.find_all("img")

print(find_all_ex1)

image1, image2 = soup.find_all("img")
find_name_ex1 = image1.name
find_name_ex2 = image2.name

print(find_name_ex1)
print(find_name_ex2)

img_dic_1 = image1["src"]
img_dic_2 = image2["src"]

print(img_dic_1)
print(img_dic_2)

title = soup.title

print(title)

title_string = soup.title.string

print(title_string)

find_all_ex2 = soup.find_all("img", src="/static/dionysus.jpg")

print(find_all_ex2)
```

```console
Profile: Dionysus





Name: Dionysus

Hometown: Mount Olympus

Favorite animal: Leopard

Favorite Color: Wine




[<img src="/static/dionysus.jpg"/>, <img src="/static/grapes.png"/>]
img
img
/static/dionysus.jpg
/static/grapes.png
<title>Profile: Dionysus</title>
Profile: Dionysus
[<img src="/static/dionysus.jpg"/>]
```

---

Part 2 테스트>

```python
from urllib.request import urlopen
from bs4 import BeautifulSoup

base_url = "http://olympus.realpython.org"

html_page = urlopen(base_url + "/profiles")
html_text = html_page.read().decode("utf-8")

soup = BeautifulSoup(html_text, "html.parser")

for link in soup.find_all("a"):
    link_url = base_url + link["href"]
    print(link_url)
```

```console
http://olympus.realpython.org/profiles/aphrodite
http://olympus.realpython.org/profiles/poseidon
http://olympus.realpython.org/profiles/dionysus
```

</div>
</details>

---

# Part3 HTML 양식과 상호 작용

<details>
<summary>Ch1 ~ Ch2 + Test Code</summary>
<div markdown="1">

Ch1> 브라우저 객체 만들기
```python
import mechanicalsoup

browser = mechanicalsoup.Browser()

url = "http://olympus.realpython.org/login"
page = browser.get(url)

print(page)

print(type(page.soup))

print(page.soup)
```

```console
<Response [200]>

<class 'bs4.BeautifulSoup'>

<html>

<head>
    <title>Log In</title>
</head>

<body bgcolor="yellow">
    <center>
        <br /><br />
        <h2>Please log in to access Mount Olympus:</h2>
        <br /><br />
        <form action="/login" method="post" name="login">
            Username: <input name="user" type="text" /><br />
            Password: <input name="pwd" type="password" /><br /><br />
            <input type="submit" value="Submit" />
        </form>
    </center>
</body>

</html>
```

---

Ch2> MechanicalSoup과 함께 양식 제출

```python
import mechanicalsoup

browser = mechanicalsoup.Browser()
url = "http://olympus.realpython.org/login"
login_page = browser.get(url)
login_html = login_page.soup

form = login_html.select("form")[0]
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

profiles_page = browser.submit(form, login_page.url)

print(profiles_page.url)

links = profiles_page.soup.select("a")

for link in links:
    address = link["href"]
    text = link.text

    print(f"{text}: {address}")

base_url = "http://olympus.realpython.org"

for link in links:
    address = base_url + link["href"]
    text = link.text

    print(f"{text}: {address}")

```

```console
http://olympus.realpython.org/profiles
Aphrodite: /profiles/aphrodite
Poseidon: /profiles/poseidon
Dionysus: /profiles/dionysus
Aphrodite: http://olympus.realpython.org/profiles/aphrodite
Poseidon: http://olympus.realpython.org/profiles/poseidon
Dionysus: http://olympus.realpython.org/profiles/dionysus
```

---

Part 3 테스트>

```python
import mechanicalsoup

browser = mechanicalsoup.Browser()

login_url = "http://olympus.realpython.org/login"
login_page = browser.get(login_url)
login_html = login_page.soup

form = login_html.form
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

profiles_page = browser.submit(form, login_page.url)

print(profiles_page.soup.title)
```

```console
<title>All Profiles</title>
```

</div>
</details>

---

# Part4 실시간으로 웹 사이트와 상호 작용

<details>
<summary>Ch1 Code</summary>
<div markdown="1">

Ch1> 실시간으로 웹 사이트와 상호 작용

```python
import mechanicalsoup
import time

browser = mechanicalsoup.Browser()
page = browser.get("http://olympus.realpython.org/dice")
tag = page.soup.select("#result")[0]
result = tag.text

print(f"The result of your dice roll is: {result}")

print("I'm about to wait for five seconds...")
time.sleep(5)
print("Done waiting!")

browser = mechanicalsoup.Browser()

for i in range(4):
    page = browser.get("http://olympus.realpython.org/dice")
    tag = page.soup.select("#result")[0]
    result = tag.text
    print(f"The result of your dice roll is: {result}")
    time.sleep(10)

browser = mechanicalsoup.Browser()

for i in range(4):
    page = browser.get("http://olympus.realpython.org/dice")
    tag = page.soup.select("#result")[0]
    result = tag.text
    print(f"The result of your dice roll is: {result}")

    if i < 3:
        time.sleep(10)
```

```console
The result of your dice roll is: 1
I'm about to wait for five seconds...
Done waiting!
The result of your dice roll is: 1
The result of your dice roll is: 2
The result of your dice roll is: 4
The result of your dice roll is: 3
The result of your dice roll is: 6
The result of your dice roll is: 3
The result of your dice roll is: 6
The result of your dice roll is: 4
```
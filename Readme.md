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

```shell
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

---

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

```shell
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

```shell
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

```shell
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

```shell
Profile: Dionysus
```

---
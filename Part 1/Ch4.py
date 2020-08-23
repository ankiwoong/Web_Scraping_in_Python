import re
from urllib.request import urlopen

# .find() 방법은 여기서 모순을 다루는 데 어려움을 겪겠지만, 정규식을 교묘하게 사용하면 이 코드를 빠르고 효율적으로 처리할 수 있다.
url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")

# 오프닝 태그를 html로 매칭한다.
# .*?과 일치한다.INGERCASE, 그리고 .*?는 이후의 어떤 텍스트와도 일치한다.
pattern = "<title.*?>.*?</title.*?>"

match_results = re.search(pattern, html, re.IGNORECASE)

title = match_results.group()
title = re.sub("<.*?>", "", title)  # Remove HTML tags

# 출력
print(title)

# urlib.properties 모듈에서 urlopen 함수 가져오기
from urllib.request import urlopen

# URL을 열고 urlopen()으로 반환된 HTTPRespontse 객체의 .read() 메서드를 사용하여 페이지의 HTML을 읽으십시오.
url = "http://olympus.realpython.org/profiles/dionysus"

html_page = urlopen(url)

# .read()는 바이트 문자열을 반환하므로, UTF-8 인코딩을 사용하여 바이트를 디코딩하려면 .decode()를 사용하십시오.
html_text = html_page.read().decode("utf-8")

for string in ["Name: ", "Favorite Color:"]:
    # html_text.find()를 사용하여 문자열의 시작 인덱스("이름:" 또는 "즐겨찾기 색상:")를 찾은 다음 string_start_idx에 인덱스를 할당하십시오.
    string_start_idx = html_text.find(string)
    # 추출할 텍스트는 "Name:" 또는 "Favorite Color:"에서 콜론 바로 뒤에 시작되므로 start_idx에 문자열 길이를 추가하여 콜론 바로 뒤에 문자의 인덱스 결과를 text_start_idx에 할당한다.
    text_start_idx = string_start_idx + len(string)

    # text_start_idx에 상대적인 첫 번째 괄호(<)의 색인을 결정하여 추출할 텍스트의 끝 색인을 계산하고 이 값을 next_html_tag_offset에 할당한다.
    # 그런 다음 text_start_idx에 값을 추가하고 결과를 text_end_idx에 할당하십시오.
    next_html_tag_offset = html_text[text_start_idx:].find("<")
    text_end_idx = text_start_idx + next_html_tag_offset

    # text_start_idx에서 text_end_idx로 html_text를 잘라서 텍스트를 추출하고 이 문자열을 raw_text에 할당한다.
    raw_text = html_text[text_start_idx:text_end_idx]

    # .strip()을 사용하여 Raw_text의 시작과 끝에서 공백을 제거하고 clean_text에 결과를 할당하십시오.
    clean_text = raw_text.strip(" \r\n\t")

    print(clean_text)

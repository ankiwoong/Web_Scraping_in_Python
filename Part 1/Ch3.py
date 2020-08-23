import re

# findall()을 사용하여 주어진 정규식과 일치하는 문자열 내에서 텍스트를 찾으십시오.
find_all_ex1 = re.findall("ab*c", "ac")

# 출력
print(find_all_ex1)

# 동일 패턴
find_all_ex2 = re.findall("ab*c", "abcd")
find_all_ex3 = re.findall("ab*c", "acc")
find_all_ex4 = re.findall("ab*c", "abcac")
find_all_ex5 = re.findall("ab*c", "abdc")

# 출력
print(find_all_ex2)
print(find_all_ex3)
print(find_all_ex4)
print(find_all_ex5)

# 패턴 매칭은 대소문자를 구분한다.
# 대소문자와 관계없이 이 패턴을 일치시키려면 re 값을 사용하여 세 번째 인수를 전달하면 된다.
find_all_ex6 = re.findall("ab*c", "ABC")
find_all_ex7 = re.findall("ab*c", "ABC", re.IGNORECASE)

# 출력
print(find_all_ex6)
print(find_all_ex7)

# 마침표(.)를 사용하여 정규식의 단일 문자를 나타낼 수 있다.
# 예를 들어 문자 "a"와 "c"가 포함된 모든 문자열을 단일 문자로 구분하여 다음과 같이 찾을 수 있다.
find_all_ex7 = re.findall("a.c", "abc")
find_all_ex8 = re.findall("a.c", "abbc")
find_all_ex9 = re.findall("a.c", "ac")
find_all_ex10 = re.findall("a.c", "acc")

# 출력
print(find_all_ex7)
print(find_all_ex8)
print(find_all_ex9)
print(find_all_ex10)

# 정규 표현식 안의 패턴 .*은 임의의 횟수를 반복하는 문자를 의미한다.
# 예를 들어, "a.*c"는 "a"로 시작하고 "c"로 끝나는 모든 하위 문자열을 찾는 데 사용될 수 있으며,
# 어떤 문자(또는 문자)가 다음 사이에 있는지와 무관하다.
find_all_ex11 = re.findall("a.*c", "abc")
find_all_ex12 = re.findall("a.*c", "abbc")
find_all_ex13 = re.findall("a.*c", "ac")
find_all_ex14 = re.findall("a.*c", "acc")

# 출력
print(find_all_ex11)
print(find_all_ex12)
print(find_all_ex13)
print(find_all_ex14)

# re.search()를 사용하여 문자열 내의 특정 패턴을 검색하는 경우가 많습니다.
# 이 함수는 서로 다른 데이터 그룹을 저장하는 MatchObject라는 개체를 반환하기 때문에 re.findall()보다 다소 복잡합니다.
# 그 이유는 다른 일치 항목 내에 일치 항목이 있을 수 있으며 re.search()가 가능한 모든 결과를 반환하기 때문입니다.
# MatchObject의 세부 정보는 여기서 중요하지 않습니다.
# 지금은 MatchObject에서 .group()을 호출하면 첫 번째 및 가장 포괄적인 결과가 반환되며, 대부분의 경우 원하는 결과가 반환됩니다.
match_results = re.search("ab*c", "ABC", re.IGNORECASE)
match_results_group = match_results.group()

# 출력
print(match_results_group)

# re 모듈에는 텍스트를 구문 분석하는 데 유용한 기능이 하나 더 있습니다.
# 대체의 줄임말인 re.sub()를 사용하면 정규식과 새 텍스트가 일치하는 문자열의 텍스트를 바꿀 수 있습니다.
# .replace() 문자열 메서드와 같이 동작합니다.
# re.sub()에 전달된 인수는 정규식 다음에 교체 텍스트를 입력하고 문자열을 따릅니다.
string = "Everything is <replaced> if it's in <tags>."
string = re.sub("<.*>", "ELEPHANTS", string)

# 출력
print(string)

# re.submessage는 정규식 "<를 사용합니다.
# *>"는 <<replaced>의 시작부터 <tags>의 끝까지 이어지는 <첫 번째>와 <마지막> 사이의 모든 것을 찾아 교체하는 것입니다.
# 왜냐하면 파이썬의 정규식은 욕심이 많아서 *와 같은 문자를 사용할 때 가능한 가장 긴 짝을 찾으려고 노력하기 때문입니다.
# 또는 가능한 가장 짧은 텍스트 문자열과 일치한다는 점을 제외하고 *와 동일한 방식으로 작동하는 *? 비자유 일치 패턴을 사용할 수 있습니다.
string2 = "Everything is <replaced> if it's in <tags>."
string2 = re.sub("<.*?>", "ELEPHANTS", string2)

# 출력
print(string2)

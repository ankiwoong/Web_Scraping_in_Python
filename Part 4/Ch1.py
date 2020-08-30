import mechanicalsoup
import time

# 먼저 /dice 페이지를 열고 결과를 스크랩한 다음 콘솔에 인쇄하는 간단한 프로그램을 작성하십시오.
browser = mechanicalsoup.Browser()
page = browser.get("http://olympus.realpython.org/dice")
tag = page.soup.select("#result")[0]
result = tag.text

print(f"The result of your dice roll is: {result}")

# sleep()이 어떻게 작용하는지를 보여주는 예
print("I'm about to wait for five seconds...")
time.sleep(5)
print("Done waiting!")

# 첫 번째 인쇄() 함수가 실행된 지 5초가 지나서야 "대기 완료!" 메시지가 표시되는 것을 알 수 있다.
# 주사위 굴리기 예제의 경우, 수면()을 위해 숫자 10을 통과해야 한다.
browser = mechanicalsoup.Browser()

for i in range(4):
    page = browser.get("http://olympus.realpython.org/dice")
    tag = page.soup.select("#result")[0]
    result = tag.text
    print(f"The result of your dice roll is: {result}")
    time.sleep(10)

# if 문을 사용하여 실행 시간을 지정함으로써 이 작업을 중지할 수 있다.
browser = mechanicalsoup.Browser()

for i in range(4):
    page = browser.get("http://olympus.realpython.org/dice")
    tag = page.soup.select("#result")[0]
    result = tag.text
    print(f"The result of your dice roll is: {result}")

    # Wait 10 seconds if this isn't the last request
    if i < 3:
        time.sleep(10)

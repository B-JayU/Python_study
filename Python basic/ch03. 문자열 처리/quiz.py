# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오.
# 예) https://naver.com
# 규칙1 : https:// 부분은 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'c' 갯수 + "!"로 구성

address = "https://www.acmicpc.net"
adr = address.replace("https://www.", "")
print(adr)
idx = adr.index(".");
print(idx)
adr = adr[:idx]
print(adr)
password = adr[:3] + str(len(adr)) + str(adr.count("c")) + "!"
print(password)
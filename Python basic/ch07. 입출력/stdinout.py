# -*- coding: EUC-KR -*-
import sys
# print("Python", "Java", "Javascript", sep=",", end="?\n")
# print("무엇이 더 재밌을까요?")
# lang = input()

# if (lang == "Javascript"):
#     print("자바 스크립트 언어")
# elif (lang == "Java"):
#     print("자바는 객체 지향 언어")
# elif (lang == "Python"):
#     print("파이썬 프로그래밍")
# else:
#     print("잘못된 입력")

# print("Python", "Java", file=sys.stdout)
# print("Python", "Java", file=sys.stderr)

scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")

# 은행 대기순번표
# 001, 002, 003, ...
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))

answer = input("아무 값이나 입력하세요 : ")
print(type(answer))



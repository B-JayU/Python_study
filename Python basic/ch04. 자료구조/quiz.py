# Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
#       참석률을 높이기 위해 댓글 이벤틑를 진행하기로 하였습니다.
#       댓글 작성자들 중에 추첨을 ㅌ오해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
#       추첨 프로그램을 작성하시오.

#       조건 1: 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
#       조건 2: 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
#       조건 3: random 모듈의 shuffle 과 sample을 활용

#       (출력 예제)
#       -- 당첨자 발표 --
#       치킨 당첨자 :
#       커피 당첨자 :
#       -- 축하합니다 --

#       (예제 구현)

from random import *
lst = range(1,21)
lst = list(lst)

shuffle(lst)
print("-- 당첨자 발표 --")
winners = sample(lst, 4)
chicken = winners[0];
print("치킨 당첨자 : {}".format(chicken))
coffee = winners[1:]
print("커피 당첨자 : {}".format(coffee))
print("-- 축하합니다 --")
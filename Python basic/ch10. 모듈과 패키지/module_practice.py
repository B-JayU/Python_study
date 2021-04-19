# -*- coding: EUC-KR -*-

# module : 필요한 것들끼리 부품처럼 만들어진 파일
# 함수정의나 클래스를 담고 있는 파일을 모듈이라 한다.

# import theater_module as mv

# theater_module.price(3) # 3명이서 영화 보러 갔을 때 가격
# theater_module.price_morning(4) # 4명이서 조조 할인 영화 보러 갔을 때
# theater_module.price_soldier(5) # 5명의 군인이 영화 보러 갔을 때

# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import *
# price(3)
# price_morning(4)
# price_soldier(5)

from theater_module import price, price_morning
price(5)
price_morning(6)

from theater_module import price_soldier as price
price(5)


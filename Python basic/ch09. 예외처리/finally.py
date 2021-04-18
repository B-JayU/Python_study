# -*- coding: EUC-KR -*-
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
        
    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    if num1 >= 10:
        raise BigNumberError("입력값 : {0}".format(num1))


    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num2 >= 10:
        raise BigNumberError(" 입력값 : {1]".format(num2))
        # 자바에서 throw error 하는 것과 동일한 개념이다
        
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))


# 예외 처리부
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
    print(err)
except ZeroDivisionError:
    print("잘못된 값을 입력하였습니다. 0으로 나눌 수 없습니다.")
finally:
    print("계산기를 이용해 주셔서 감사합니다.")
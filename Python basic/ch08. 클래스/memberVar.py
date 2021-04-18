# -*- coding: EUC-KR -*-
class Unit:
    
    # 객체 생성자 함수
    def __init__(self, name, hp, damage):
        # 멤버 변수 : 클래스 내에서 선언된 변수
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력{1}".format(self.hp, self.damage))


# 객체 instance 생성하기
marine1 = Unit("마린1", 40, 12)
marine2 = Unit("마린2", 37, 23)
marine3 = Unit("마린3", 87, 1)
tank1 = Unit("탱크1", 54, 4)
tank2 = Unit("탱크2", 24, 13)

wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 :{1}".format(wraith1.name, wraith1.damage))


wraith2 = Unit("레이스", 80, 5)
# 객체의 추가 멤버 변수를 추가할 수 있다.
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))
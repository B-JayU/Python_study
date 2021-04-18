# -*- coding: EUC-KR -*-
class Unit:
    
    # 객체 생성자 함수
    def __init__(self, name, hp, damage):
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




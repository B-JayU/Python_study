# -*- coding: EUC-KR -*-
# 일반 유닛
class Unit:    
    # 객체 생성자 함수
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력{1}".format(self.hp, self.damage))

# 공격 유닛
# 괄호를 생성하고 상속받고자 하는 상위클래스를 괄호 안에 명시한다. 
class AttackUnit(Unit):
    # 일반 유닛에도 코드 라인이 존재함.
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력{1}".format(self.hp, self.damage))
    
    def attack(self, location):
        print("{0} : {1} 방향으로 적군으로 공격 합니다. [공격력 {2}]" \
            .format(self.name, location, self.damage))
    
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))

        if self.hp <= 0:
            print("{0} : 파괴 되었습니다.".format(self.name))
        

firebat1 = AttackUnit("파이어뱃1", 50, 16)
firebat1.attack("5시")
firebat1.damaged(25)
firebat1.damaged(25)
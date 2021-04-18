# -*- coding: EUC-KR -*-
# 일반 유닛
# 부모 클래스
class Unit:    
    # 객체 생성자 함수
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        # self.damage = damage
        # print("{0} 유닛이 생성 되었습니다.".format(self.name))
        # print("체력 {0}, 공격력{1}".format(self.hp, self.damage))

# 공격 유닛
# 자식 클래스
# 괄호를 생성하고 상속받고자 하는 상위클래스를 괄호 안에 명시한다. 
class AttackUnit(Unit):
    # 일반 유닛에도 코드 라인이 존재함.
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
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
        
# 드랍쉽 : 공중 유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수송. 공격x
class Flyable():
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]" \
            .format(name, location, self.flying_speed))

#공중 공격 유닛 클래스 (다중 상속 받은 클래스)
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

firebat1 = AttackUnit("파이어뱃1", 50, 16)
firebat1.attack("5시")
firebat1.damaged(25)
firebat1.damaged(25)

# 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "5시")
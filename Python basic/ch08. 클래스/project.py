# -*- coding: EUC-KR -*-
# �Ϲ� ����
# �θ� Ŭ����
from random import *

class Unit:    
    # ��ü ������ �Լ�
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} ������ �����Ǿ����ϴ�.".format(self.name))
        # self.damage = damage
        # print("ü�� {0}, ���ݷ�{1}".format(self.hp, self.damage))
    
    def move(self, location):
        print("[���� ���� �̵�]")
        print("{0} : {1} �������� �̵��մϴ�. [�ӵ� {2}]".format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0} : {1} �������� �Ծ����ϴ�.".format(self.name, damage))
        self.hp -= damage
        print("{0} : ���� ü���� {1} �Դϴ�.".format(self.name, self.hp))

        if self.hp <= 0:
            print("{0} : �ı� �Ǿ����ϴ�.".format(self.name))

# ���� ����
# �ڽ� Ŭ����
# ��ȣ�� �����ϰ� ��ӹް��� �ϴ� ����Ŭ������ ��ȣ �ȿ� ����Ѵ�. 
class AttackUnit(Unit):
    # �Ϲ� ���ֿ��� �ڵ� ������ ������.
    def __init__(self, name, hp, damage, speed):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
        print("{0} ������ ���� �Ǿ����ϴ�.".format(self.name))
        print("ü�� {0}, ���ݷ�{1}".format(self.hp, self.damage))
    
    def attack(self, location):
        print("{0} : {1} �������� �������� ���� �մϴ�. [���ݷ� {2}]" \
            .format(self.name, location, self.damage))

class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "����", 40, 1, 5)

        #������ : ���� �ð� ���� �̵� �� ���� �ӵ��� ����, ü�� 10 ����

    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : �������� ����մϴ�. (HP 10 ����)".format(self.name))
        else:
            print("{0} : ü���� �����Ͽ� �������� ������� �ʽ��ϴ�.".format(self.name))

class Tank(AttackUnit):
    # ������ : ��ũ�� ���� ��������, �� ���� �Ŀ��÷� ���� ���� �̵� �Ұ�.
    seize_developed = False # ������ ���߿���

    def __init__(self):
        AttackUnit.__init__(self, "��ũ", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return

        if self.seize_mode == False:
            print("{0} : ������� ��ȯ�մϴ�.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        else:
            print("{0} : �����带 �����մϴ�.".format(self.name))
            self.damage /= 2
            self.seize_mode = False
        
        
        
# ����� : ���� ����, ���۱�. ���� / ���̾�� / ��ũ ���� ����. ����x
class Flyable():
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} �������� ���ư��ϴ�. [�ӵ� {2}]" \
            .format(name, location, self.flying_speed))

#���� ���� ���� Ŭ���� (���� ��� ���� Ŭ����)
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage, 0) # ���� speed 0
        Flyable.__init__(self, flying_speed)

    def move(self, location): # Unit Ŭ������ �ִ� move�� ������
        print("[���� ���� �̵�]")
        self.fly(self.name, location)

class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "���̽�", 80, 20, 5)
        self.clocked = False # Ŭ��ŷ ��� (���� ����)

    def clocking(self):
        if self.clocked == True:
            print("{0} : Ŭ��ŷ ��带 �����մϴ�.".format(self.name))
            self.clocked = False
        else:
            print("{0} : Ŭ��ŷ ��带 �����մϴ�.".format(self.name))
            self.clocked = True



class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0)
        self.location = location

supply_depot = BuildingUnit("���ö��� ����", 500, "7��")

def game_start():
    print("[�˸�] ���ο� ������ �����մϴ�.")

def game_over():
    print("player : gg")
    print("[Player]���� �����ϼ̽��ϴ�.")

game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()
w2 = Wraith()

attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)
attack_units.append(w2)

for unit in attack_units:
    unit.move("1��")

Tank.seize_developed = True
print("[�˸�] ��ũ ���� ��� ������ �Ϸ�Ǿ����ϴ�.")

for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

for unit in attack_units:
    unit.attack("1��")


for unit in attack_units:
    unit.damaged(randint(5,21))
game_over()
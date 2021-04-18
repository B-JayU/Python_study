# -*- coding: EUC-KR -*-
# �Ϲ� ����
# �θ� Ŭ����
class Unit:    
    # ��ü ������ �Լ�
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        # self.damage = damage
        # print("{0} ������ ���� �Ǿ����ϴ�.".format(self.name))
        # print("ü�� {0}, ���ݷ�{1}".format(self.hp, self.damage))
    
    def move(self, location):
        print("[���� ���� �̵�]")
        print("{0} : {1} �������� �̵��մϴ�. [�ӵ� {2}]".format(self.name, location, self.speed))


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
    
    def damaged(self, damage):
        print("{0} : {1} �������� �Ծ����ϴ�.".format(self.name, damage))
        self.hp -= damage
        print("{0} : ���� ü���� {1} �Դϴ�.".format(self.name, self.hp))

        if self.hp <= 0:
            print("{0} : �ı� �Ǿ����ϴ�.".format(self.name))
        
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
        AttackUnit.__init__(self, name, hp,damage, 0) # ���� speed 0
        Flyable.__init__(self, flying_speed)

    def move(self, location): # Unit Ŭ������ �ִ� move�� ������
        print("[���� ���� �̵�]")
        self.fly(self.name, location)


class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0)
        self.location = location

supply_depot = BuildingUnit("���ö��� ����", 500, "7��")

def game_start():
    print("[�˸�] ���ο� ������ �����մϴ�.")

def game_over():
    pass

game_start()
game_over()

firebat1 = AttackUnit("���̾��1", 50, 16, 13)
firebat1.attack("5��")
firebat1.damaged(25)
firebat1.damaged(25)

# ��Ű�� : ���� ���� ����, �ѹ��� 14�� �̻��� �߻�
valkyrie = FlyableAttackUnit("��Ű��", 200, 6, 5)
valkyrie.fly(valkyrie.name, "5��")

# ���� : ���� ����, �⵿���� ����
vulture = AttackUnit("����", 80, 10, 20)

# ��Ʋũ���� : ���� ����, ü�µ� ������ ����, ���ݷµ� ����
battlecruiser = FlyableAttackUnit("��Ʋũ����", 500, 25, 3)

vulture.move("11��") # �θ� Ŭ������ Unit Ŭ������ move�Լ��� ȣ��
battlecruiser.move("11��") # FlyableAttackUnit���� move�� �������Ͽ���.

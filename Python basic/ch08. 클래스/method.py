# -*- coding: EUC-KR -*-
# �Ϲ� ����
class Unit:    
    # ��ü ������ �Լ�
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} ������ ���� �Ǿ����ϴ�.".format(self.name))
        print("ü�� {0}, ���ݷ�{1}".format(self.hp, self.damage))

# ���� ����
# ��ȣ�� �����ϰ� ��ӹް��� �ϴ� ����Ŭ������ ��ȣ �ȿ� ����Ѵ�. 
class AttackUnit(Unit):
    # �Ϲ� ���ֿ��� �ڵ� ������ ������.
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
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
        

firebat1 = AttackUnit("���̾��1", 50, 16)
firebat1.attack("5��")
firebat1.damaged(25)
firebat1.damaged(25)
# -*- coding: EUC-KR -*-
class Unit:
    
    # ��ü ������ �Լ�
    def __init__(self, name, hp, damage):
        # ��� ���� : Ŭ���� ������ ����� ����
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} ������ ���� �Ǿ����ϴ�.".format(self.name))
        print("ü�� {0}, ���ݷ�{1}".format(self.hp, self.damage))


# ��ü instance �����ϱ�
marine1 = Unit("����1", 40, 12)
marine2 = Unit("����2", 37, 23)
marine3 = Unit("����3", 87, 1)
tank1 = Unit("��ũ1", 54, 4)
tank2 = Unit("��ũ2", 24, 13)

wraith1 = Unit("���̽�", 80, 5)
print("���� �̸� : {0}, ���ݷ� :{1}".format(wraith1.name, wraith1.damage))


wraith2 = Unit("���̽�", 80, 5)
# ��ü�� �߰� ��� ������ �߰��� �� �ִ�.
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0}�� ���� Ŭ��ŷ �����Դϴ�.".format(wraith2.name))
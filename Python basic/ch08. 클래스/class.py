# -*- coding: EUC-KR -*-

# ���� : ���� ����, ����. ���� �� �� ����

name = "����" # ������ �̸�
hp = 40 # ������ ü��
damage = 5 # ������ ���ݷ�

print("{0} ������ �����Ǿ����ϴ�.".format(name))
print("ü�� {0}, ���ݷ� {1}\n".format(hp, damage))

# ��ũ : ���� ����, ��ũ, ���� �� �� �ִµ�, �Ϲ� ��� / ���� ���
tank_name = "��ũ"
tank_hp = 150
tank_damage = 35

print("{0} ������ �����Ǿ����ϴ�.".format(tank_name))
print("ü�� {0}, ���ݷ� {1}\n".format(tank_hp,tank_damage))


tank2_name = "��ũ2"
tank2_hp = 200
tank2_damage = 50

print("{0} ������ �����Ǿ����ϴ�.".format(tank2_name))
print("ü�� {0}, ���ݷ� {1}\n".format(tank2_hp,tank2_damage))


def attack(name, location, damage):
    print("{0} : {1} �������� ������ ���� �մϴ�. [���ݷ� {2}]".format( \
        name, location, damage))

attack(name, "1��", damage)
attack(tank_name, "1��", tank_damage)
attack(tank2_name, "1��", tank2_damage)


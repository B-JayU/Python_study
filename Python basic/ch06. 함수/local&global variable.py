# -*- coding: EUC-KR -*-
gun = 10

def checkpoint(soldiers):
    global gun
    gun = gun - soldiers
    print("[�Լ� ��] ���� �� : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[�Լ� ��] ���� �� : {0}".format(gun))
    return gun

print("��ü �� : {0}".format(gun))
gun = checkpoint_ret(gun, 2)
print("���� �� : {0}".format(gun))
print(gun)
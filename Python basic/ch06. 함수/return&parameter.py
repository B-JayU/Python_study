# -*- coding: EUC-KR -*-
def open_account():
    print("���ο� ���°� �����Ǿ����ϴ�.")

def deposit(balance, money):
        # print("�Ա��� �Ϸ�Ǿ����ϴ�. �ܾ��� {0} ���Դϴ�.".format(balance + money))
        return balance + money

def withdraw(balance, money): 
    if money > balance:
        print("�ܾ��� �����մϴ�.")
        return balance
    else:
        print("{0} �� ����� �Ϸ�Ǿ����ϴ�.".format(money))
        return balance-money

def withdraw_night(balance, money):
    commission = 100 # ������ 100��
    withdraw(balance, money)
    return commission, balance - money - commission

open_account()
balance = 0
balance = deposit(balance,300000)
print("�Ա��� �Ϸ�Ǿ����ϴ�. �ܾ��� {0} ���Դϴ�.".format(balance))
# balance = withdraw(balance, 400000)
# print("�ܾ��� {0} ���Դϴ�.".format(balance))

commission, balance = withdraw_night(balance, 50000)
print("������ {0} ���̸�, �ܾ��� {1} ���Դϴ�.".format(commission, balance))

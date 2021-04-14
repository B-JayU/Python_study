# -*- coding: EUC-KR -*-
def open_account():
    print("새로운 계좌가 개설되었습니다.")

def deposit(balance, money):
        # print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
        return balance + money

def withdraw(balance, money): 
    if money > balance:
        print("잔액이 부족합니다.")
        return balance
    else:
        print("{0} 원 출금이 완료되었습니다.".format(money))
        return balance-money

def withdraw_night(balance, money):
    commission = 100 # 수수료 100원
    withdraw(balance, money)
    return commission, balance - money - commission

open_account()
balance = 0
balance = deposit(balance,300000)
print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance))
# balance = withdraw(balance, 400000)
# print("잔액은 {0} 원입니다.".format(balance))

commission, balance = withdraw_night(balance, 50000)
print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))

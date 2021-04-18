# -*- coding: EUC-KR -*-
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
        
    def __str__(self):
        return self.msg

try:
    print("�� �ڸ� ���� ������ ���� �����Դϴ�.")
    num1 = int(input("ù ��° ���ڸ� �Է��ϼ��� : "))
    if num1 >= 10:
        raise BigNumberError("�Է°� : {0}".format(num1))


    num2 = int(input("�� ��° ���ڸ� �Է��ϼ��� : "))
    if num2 >= 10:
        raise BigNumberError(" �Է°� : {1]".format(num2))
        # �ڹٿ��� throw error �ϴ� �Ͱ� ������ �����̴�
        
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))


# ���� ó����
except ValueError:
    print("�߸��� ���� �Է��Ͽ����ϴ�. �� �ڸ� ���ڸ� �Է��ϼ���.")
except BigNumberError as err:
    print("������ �߻��Ͽ����ϴ�. �� �ڸ� ���ڸ� �Է��ϼ���.")
    print(err)
except ZeroDivisionError:
    print("�߸��� ���� �Է��Ͽ����ϴ�. 0���� ���� �� �����ϴ�.")
finally:
    print("���⸦ �̿��� �ּż� �����մϴ�.")
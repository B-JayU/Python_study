# -*- coding: EUC-KR -*-

try:
    print("�� �ڸ� ���� ������ ���� �����Դϴ�.")
    num1 = int(input("ù ��° ���ڸ� �Է��ϼ��� : "))
    if num1 >= 10:
        raise ValueError

    num2 = int(input("�� ��° ���ڸ� �Է��ϼ��� : "))
    if num2 >= 10:
        raise ValueError
        # �ڹٿ��� throw error �ϴ� �Ͱ� ������ �����̴�
        
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))

except ValueError:
    print("�߸��� ���� �Է��Ͽ����ϴ�. �� �ڸ� ���ڸ� �Է��ϼ���.")
# -*- coding: EUC-KR -*-

# Quiz) ���׿� �׻� ��� �մ��� �ִ� ���ִ� ġŲ���� �ֽ��ϴ�.
# ��� �մ��� ġŲ �丮 �ð��� ���̰��� �ڵ� �ֹ� �ý����� �����Ͽ����ϴ�.
# �ý��� �ڵ带 Ȯ���ϰ� ������ ����ó�� ������ �����ÿ�.

# ����1 : 1���� �۰ų� ���ڰ� �ƴ� �Է°��� ���� ���� valueError �� ó��
#         ��� �޼��� : "�߸��� ���� �Է��Ͽ����ϴ�."
# ����2 : ��� �մ��� �ֹ��� �� �ִ� �� ġŲ���� 10������ ����
#         ġŲ ���� �� ����� ���� ����[SoldOutError]�� �߻���Ű�� ���α׷� ����
#         ��� �޽��� : "��� �����Ǿ� �� �̻� �ֹ��� ���� �ʽ��ϴ�."

# [�ڵ�]

class SoldOutError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

chicken = 10
waiting = 1 # Ȧ �ȿ��� ���� ����, ����ȣ 1���� ����
while(True):
    try:

        print("[���� ġŲ : {0}]".format(chicken))
        order = int(input("�� ������ ġŲ�� �ֹ��Ͻðڽ��ϱ�?"))
        
        if order > chicken:
            print("��ᰡ �����մϴ�.")
        elif order < 1:
            raise ValueError    
        else:
            print("[����ȣ {0}] {1} ���� �ֹ��� �Ϸ�Ǿ����ϴ�." \
                .format(waiting, order))
            waiting += 1
            chicken -= order

        if chicken == 0:
            raise SoldOutError("��� �����Ǿ� �� �̻� �ֹ��� ���� �ʽ��ϴ�.")

    except ValueError:
            print("�߸��� ���� �Է��Ͽ����ϴ�.")
    except SoldOutError as err:
        print(err)
        break
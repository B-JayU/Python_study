# -*- coding:EUC-KR -*-
try:
    print("������ ���� �����Դϴ�.")
    nums = []
    nums.append(int(input("ù ��° ���ڸ� �Է��ϼ��� : ")))
    nums.append(int(input("�� ��° ���ڸ� �Է��ϼ��� : ")))
    # nums.append(int(nums[0]/nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("����! �߸��� ���� �Է��Ͽ����ϴ�.")
except ZeroDivisionError as err:
    print(err)
    # print("����! 0���� ���� �� �����ϴ�.")
# except IndexError:
#     print("����! �߸��� �ε��� �����Դϴ�.")
except Exception as err:
    print("�� �� ���� ������ �߻��Ͽ����ϴ�.")
    print(err)

    
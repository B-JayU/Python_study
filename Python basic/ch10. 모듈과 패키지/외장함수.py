# -*- coding: EUC-KR -*-
# glob : ��� ���� ���� / ���� ��� ��ȸ (������ dir)

# import glob
# print(glob.glob("*.py")) #Ȯ���ڰ� py �� ��� ����

# # os : �ü������ �����ϴ� �⺻ ���
# import os
# print(os.getcwd())  # ���� ���丮 ǥ��

# folder = "sample.dir"

# if os.path.exists(folder):
#     print("�̹� �����ϴ� �����Դϴ�.")
#     os.rmdir(folder)
#     print("������ �����Ͽ����ϴ�.")
# else:
#     os.makedirs(folder)
#     print(folder, "������ �����Ͽ����ϴ�.")
# print(os.listdir())

import time
import datetime

print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))
today = datetime.date.today() # ���ó�¥ ����
td = datetime.timedelta(days=100) # 100�� ��
print("�츮�� ������ 100�� �Ǵ� ����", today + td)


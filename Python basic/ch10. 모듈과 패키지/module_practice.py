# -*- coding: EUC-KR -*-

# module : �ʿ��� �͵鳢�� ��ǰó�� ������� ����
# �Լ����ǳ� Ŭ������ ��� �ִ� ������ ����̶� �Ѵ�.

# import theater_module as mv

# theater_module.price(3) # 3���̼� ��ȭ ���� ���� �� ����
# theater_module.price_morning(4) # 4���̼� ���� ���� ��ȭ ���� ���� ��
# theater_module.price_soldier(5) # 5���� ������ ��ȭ ���� ���� ��

# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import *
# price(3)
# price_morning(4)
# price_soldier(5)

from theater_module import price, price_morning
price(5)
price_morning(6)

from theater_module import price_soldier as price
price(5)


# -*- coding: EUC-KR -*-
import travel.thailand # import ������ ����̳� ��Ű�� ���� �� �� ����.
#import travel.thailand.thailandPackage()
# trip_to1 = travel.thailand.ThailandPackage()
# trip_to1.detail()

# from travel import vietnam
# trip_to2 = vietnam.VietnamPackage()
# trip_to2.detail()

# from travel import *
# trip_to3 = thailand.ThailandPackage()
# trip_to3.detail()

from travel import *
import inspect
import random

#getfile() ��ȣ�ȿ� �����ϰ��� �ϴ� ������ �̸��� �Է��Ѵ�.
#getfile()�� ���, �ش� ������ ��θ� ��ȯ�Ѵ�.
print(inspect.getfile(random))
#print(inspect.getfile(thailand))


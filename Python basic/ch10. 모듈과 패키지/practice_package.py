# -*- coding: EUC-KR -*-
import travel.thailand # import 옆에는 모듈이나 패키지 들이 올 수 있음.
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

#getfile() 괄호안에 추적하고자 하는 파일의 이름을 입력한다.
#getfile()의 결과, 해당 파일의 경로를 반환한다.
print(inspect.getfile(random))
#print(inspect.getfile(thailand))


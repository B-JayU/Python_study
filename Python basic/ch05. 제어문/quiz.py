
from random import *
customer = 0
for i in range(0, 50):
    time = randint(5, 51)
    if (5 <= time <= 15):
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i+1, time))
        customer += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i+1, time))

print()
print("총 탑승 승객 : {0} 분".format(customer))

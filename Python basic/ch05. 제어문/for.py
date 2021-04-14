# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")

for waiting_no in [1, 2, 3, 4]:
    print("대기번호 : {0}".format(waiting_no))
print()

for waiting_no in range(1, 5):
    print("대기번호 : {0}".format(waiting_no))
print()

starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print("{0} 고객님, 주문하신 커피가 준비되었습니다.".format(customer))

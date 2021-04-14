# while
customer = "토르"
index = 5
while index >= 1:
    print("{0} 고객님, 커피가 준비되었습니다. {1}번 남았습니다.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피가 페기처분되었습니다.")
print()

customer = "토르"
person = "Unknown"

while person != customer:
    print("{0} 고객님, 주문하신 커피가 준비되었습니다.".format(customer))
    person = input("이름이 어떻게 되십니까? ")
    if person == customer:
        print("{0} 고객님, 맛있게 드십시오^^".format(person))
print()
id = "990120-1234567"

print("성별 : "+ id[7])
print("연 : " + id[0:2])
print("월 : " + id[2:4])
print("일 : " + id[4:6])

print("생년월일 : " + id[0:6])  # start는 포함하고 end는 포함하지 않는 범위
print("생년월일 : " + id[:6])  # start가 0인 경우, 생략 가능하다

print("뒤 7자리 : " + id[7:14])
print("뒤 7자리 : " + id[7:]) # end가 마지막 idx인 경우는 생략 가능하다
print("뒤 7자리 (역순으로) : " + id[-7:])
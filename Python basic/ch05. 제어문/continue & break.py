absent = [2, 5]  # 결석
no_book = [7]
for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업은 여기까지, {0}번 학생은 교무실로 따라와.".format(student))
        break
    print("{0}번 학생, 책을 읽어주세요".format(student))
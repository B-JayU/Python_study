# 출석번호 1, 2, 3, 4
students = [1, 2, 3, 4, 5]
print(students)

students = [i+100 for i in students]
print(students)

students = ["iron man", "thor", "groot"]
students = [len(i) for i in students]
print(students)

students = ["iron man", "thor", "groot"]
students = [i.capitalize() for i in students]
print(students)
# -*- coding: EUC-KR -*-
import sys
# print("Python", "Java", "Javascript", sep=",", end="?\n")
# print("������ �� ��������?")
# lang = input()

# if (lang == "Javascript"):
#     print("�ڹ� ��ũ��Ʈ ���")
# elif (lang == "Java"):
#     print("�ڹٴ� ��ü ���� ���")
# elif (lang == "Python"):
#     print("���̽� ���α׷���")
# else:
#     print("�߸��� �Է�")

# print("Python", "Java", file=sys.stdout)
# print("Python", "Java", file=sys.stderr)

scores = {"����":0, "����":50, "�ڵ�":100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")

# ���� ������ǥ
# 001, 002, 003, ...
for num in range(1, 21):
    print("����ȣ : " + str(num).zfill(3))

answer = input("�ƹ� ���̳� �Է��ϼ��� : ")
print(type(answer))



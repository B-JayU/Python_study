# -*- coding: EUC-KR -*-
def std_weight(height, gender):
    weight = 0
    if gender == "����":
        weight = height * height * 22
        return weight
    else:
        weight = height * height * 21
        return weight

height = 175 # cm����
gender = "����"
weight = round(std_weight(height/100, gender),2)
print("Ű {0}cm {1} �� ǥ�� ü���� {2}kg �Դϴ�.".format(height, gender, weight))
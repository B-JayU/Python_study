# -*- coding: EUC-KR -*-
def std_weight(height, gender):
    weight = 0
    if gender == "남자":
        weight = height * height * 22
        return weight
    else:
        weight = height * height * 21
        return weight

height = 175 # cm단위
gender = "남자"
weight = round(std_weight(height/100, gender),2)
print("키 {0}cm {1} 의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))
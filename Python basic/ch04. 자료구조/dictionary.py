cabinet = {3: "유재석", 100: "김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
# 오류가 발생 print(cabinet[5])
print(cabinet.get(5, "사용가능"))

print(3 in cabinet)
print(5 in cabinet)

cab = {"A-3": "유재석", "B-100": "김태호"}
print(cab["A-3"])
print(cab["B-100"]);

cab["A-3"]="김종국"
cab["C-20"] = "조세호"
print(cab);

del cab["A-3"]
print(cab);
print(cab.keys())
print(cab.values())
print(cab.items())
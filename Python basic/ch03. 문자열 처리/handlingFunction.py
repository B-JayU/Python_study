python = "Python is Amazing"
print(python.lower())  # 소문자로 나타내기
print(python.upper())  # 대문자로 나타내기
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index+1)  # 앞에서 찾은 idx 다음 위치부터 찾아서 index를 표시
print(index)

print(python.find("n"))

print(python.find("Java"))  # python 문자열 내에 "Java"가 있으면 인덱스 반환, 없으면 -1 반환
#print(python.index("Java"))  # python 문자열 내에 "Java"의 인덱스 값 반환, 없으면 오류 발생
print(python.count("n"))  # python 문자열 내에 "n"의 개수를 출력한다.

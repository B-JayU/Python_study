# -*- coding: EUC-KR -*-

"""
def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("�̸� : {0}\t���� : {1}\t".format(name, age), end=" ")
    print(lang1, lang2, lang3, lang4, lang5)
"""

def profile(name, age, *language):
    print("�̸� : {0}\t���� : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("���缮", 20, "Python", "java", "c", "c++", "C#")
profile("����ȣ", 25, "kotlin", "swift")
# -*- coding: EUC-KR -*- 

def profile(name, age, main_lang):
    print("�̸� : {0}\t���� : {1}\t�� ��� ���: {2}".format(name, age, main_lang))

def profile2(name, age=17, main_lang="Python"):
    print("�̸� : {0}\t���� : {1}\t�� ��� ���: {2}".format(name, age, main_lang))

profile("���缮", 20, "Python")
profile("����ȣ", 25, "Java")

profile2("���缮")
profile2("����ȣ")
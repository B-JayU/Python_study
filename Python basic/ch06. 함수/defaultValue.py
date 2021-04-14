# -*- coding: EUC-KR -*- 

def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}".format(name, age, main_lang))

def profile2(name, age=17, main_lang="Python"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}".format(name, age, main_lang))

profile("유재석", 20, "Python")
profile("김태호", 25, "Java")

profile2("유재석")
profile2("김태호")
# -*- coding: EUC-KR -*-
# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)

# import glob
# print(glob.glob("*.py")) #확장자가 py 인 모든 파일

# # os : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd())  # 현재 디렉토리 표시

# folder = "sample.dir"

# if os.path.exists(folder):
#     print("이미 존재하는 파일입니다.")
#     os.rmdir(folder)
#     print("폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder)
#     print(folder, "폴더를 생성하였습니다.")
# print(os.listdir())

import time
import datetime

print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))
today = datetime.date.today() # 오늘날짜 저장
td = datetime.timedelta(days=100) # 100일 후
print("우리가 만난지 100일 되는 날은", today + td)


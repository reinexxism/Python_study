# datetime 모듈의 사용법
# 1. 가장 먼저 import 명령을 통해 datetime module을 가져온다.
import datetime
today = datetime.date.today() # datetime : module / date : class / today() : method

print(today)
print(today.year) # 오늘의 연도만을 확인하고자 할 때
print(today.month) # 오늘의 달만을 확인하고자 할 때
print(today.day) # 오늘의 날짜만을 확인하고자 할 때

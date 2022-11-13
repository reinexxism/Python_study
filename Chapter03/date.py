# 날짜 / 시간과 관련된 기능을 가져온다.
import datetime

# 현재 날짜 / 시간을 구한다.
now = datetime.datetime.now()

# Output
print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")
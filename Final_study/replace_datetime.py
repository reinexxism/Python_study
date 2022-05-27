# 현재 날짜 및 시간 변경
# imiport [모듈명] as [모듈 별칭]
import datetime as dt
start_time = dt.datetime.now()
start_time2 = start_time.replace(month = 12, day = 25)

print(start_time2)
# 오늘의 날짜와 현재 시간 출력하기
import datetime as dt

start_day = dt.date.today()
year = start_day.year
month = start_day.month
day = start_day.day

print('오늘의 날짜 : {}년 {}월 {}일'.format(year, month, day))


start_time = dt.datetime.now()
hour = start_time.hour
minute = start_time.minute
second = start_time.second

if hour < 12 :
  print('현재시간 : 오전 {}시 {}분 {}초'.format(hour, minute, second))
else : 
  hour = hour - 12
  print('현재시간 : 오후 {}시 {}분 {}초'.format(hour, minute, second))



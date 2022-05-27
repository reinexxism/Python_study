import datetime as dt

today = dt.date.today()
print('오늘은 {}년 {}월 {}일입니다.'.format(today.year, today.month, today.day))

newYear = dt.datetime(2036, 1, 1)
time_gap = newYear - dt.datetime.now()
print('2036년 새해까지는 {}일 {}시간 남았습니다.'.format(time_gap.days, time_gap.seconds //3600))
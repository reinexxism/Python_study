import datetime as dt

today = dt.date.today()
print('오늘은 {}년 {}월 {}일입니다.'.format(today.year, today.month, today.day))

birthDay = dt.datetime(2022, 8, 5)
time_gap = birthDay - dt.datetime.now()
print('2020년 생일까지는 {}일 {}시간 남았습니다.'.format(time_gap.days, time_gap.seconds // 3600))

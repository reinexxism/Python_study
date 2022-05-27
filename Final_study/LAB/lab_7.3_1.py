import datetime as dt

today = dt.date.today()
print('오늘은 {}년 {}월 {}일입니다.'.format(today.year, today.month, today.day))

senNichi = dt.timedelta(days = 1000)
plus1000day = dt.datetime.now() + senNichi
print('1000일 후 : ', plus1000day)
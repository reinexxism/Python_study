import datetime as dt

a, b, c = map(int, input('처음으로 사귄 연도와 월, 일을 입력하시오 : ').split())
firstDay = dt.datetime(a, b, c)

hundred = dt.timedelta(days = 100)
plus100day = firstDay + hundred
print('100일 기념일은 : {}년 {}월 {}일입니다.'.format(plus100day.year, plus100day.month, plus100day.day))
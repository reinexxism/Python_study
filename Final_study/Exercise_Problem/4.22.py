import datetime as dt
date = dt.datetime.now()
# print(date)

y, m, d = date.year, date.month, date.day
print('현재 시간은 {}년 {}월 {}일입니다.'.format(y, m, d))
print('지금 태어난 아이의 주민등록번호 앞자리는 : {}{:02d}{:02d}'.format(str(y)[2:4], m, d))
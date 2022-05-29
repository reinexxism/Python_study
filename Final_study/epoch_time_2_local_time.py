# time.time()을 통한 현재시간 출력
import time

unix_timestamp = time.time()
loal_time = time.localtime(unix_timestamp)
print(time.strftime('%Y-%m-%d %H:%M:%S', loal_time))
# time module의 strftime() 함수는 localtime() 함수가 반환한 'struct_time'이라는 형식의 
# 튜플 값을 지정된 포맷의 문자열로 변환시키는 기능

# try-except 문을 사용한 구체적인 예외처리
try :
  b = 2 / 0 # 만약 주석처리한다면 TypeError에 대한 대처만 출력된다.
  a = 1 + 'hundred'
except ZeroDivisionError :
  print('0으로 나누는 오류 발생')
except TypeError :
  print('지원되지 않는 연산자를 사용하는 오류 발생')
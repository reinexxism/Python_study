# try-except-else-finally 구문의 사용법
def divide(x, y) :
  try :
    result = x / y
  except ZeroDivisionError :
    print('0으로 나누는 오류발생')
  else :
    print('결과 : ', result)
  finally :
    print('수행 완료')

print('divide(100, 2) 함수호출 : ')
divide(100, 2)
print('divide(100, 0) 함수호출 : ')
divide(100, 0)

# 사용자로부터 입력받은 다섯 개의 정수를 저장하는 프로그램
f = open('data5.txt', 'w') # 파일을 생성하고 쓰기 모드로 연다.

for i in range(5) :
  n = input('정수를 입력하세요 : ')
  f.write(n) # 파일에 입력된 정수를 문자열로 쓰기
  f.write('\n') # 파일에 정수를 쓴 후 줄바꿈하기
f.close()
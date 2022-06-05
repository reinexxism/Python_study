# 파일로부터 정수를 입력받아 합과 평균을 계산
f = open('data5.txt', 'r') # 읽기 모드로 파일을 열기
su = 0

for i in range(5) :
  n = int(f.readline()) # data5.txt 파일의 한 줄 내의 숫자를 읽어서
  su += n # su에 누적해서 더한다.

print('다섯 숫자의 합 : {}, 평균 : {}'.format(su, su /5)) # 합과 평균을 출력
f.close()
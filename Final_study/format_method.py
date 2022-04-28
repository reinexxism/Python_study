# 정수 표현을 위한 기본 포매팅
for i in range(2, 15, 2):  
  print('{0} {1} {2}'.format(i, i*i, i*i*i)) 

# 출력 칸의 크기 지정을 통한 정수 포매팅
for i in range(2, 15, 2):
  print('{0:3d} {1:4d} {2:5d}'.format(i, i*i, i*i*i)) 

# 소수점 아래 자리수를 조절하는 실수 포매팅
print('소수점 두 자리로 표현한 원주율 = {0:10.2f}'.format(3.1415926))
print('소수점 세 자리로 표현한 원주율 = {0:10.3f}'.format(3.1415926))
print('소수점 네 자리로 표현한 원주율 = {0:10.4f}'.format(3.1415926))

# 실수 표현을 위한 포매팅에서 소수점
print('1/3은 {:.3f}'.format(1/3)) 

# 1000단위 쉼표 출력방법
print('{:,}'.format(1234567890))

# placeholder내에 키-값 형식으로 인자를 전달하는 방법
print('위도 : {0}, 경도 : {1}'.format('35.17N', '129.07E'))
print('위도 : {lat}, 경도 : {long}'.format(lat = '35.17E', long = '129.07E'))
print('위도 : {lat}, 경도 : {long}'.format(long = '129.07E', lat = '35.17N')) #순서에 상관없이 출력 가능
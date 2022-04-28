x, y = map(int,input('점의 좌표 x, y를 입력하세요 : ').split())

if (x * x + y * y > 25):
  print('원의 외부에 있음')
elif (x * x + y * y <= 25):
  print('원의 내부에 있음')
x, y = map(int,input('점의 좌표 x, y를 입력하시오 : ').split())

if (x * x + y * y - 6 * x - 8 * y > 75):
  print('원의 외부에 있음')
elif ( x * x + y * y - 6 * x - 8 * y <= 75):
  print('원의 내부에 있음')
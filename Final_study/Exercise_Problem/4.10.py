x1 = int(input('x1 좌표를 입력하세요 : '))
y1 = int(input('y1 좌표를 입력하세요 : '))
x2 = int(input('x2 좌표를 입력하세요 : '))
y2 = int(input('y2 좌표를 입력하세요 : '))

def distance(x1, y1, x2, y2):
  result = 0;
  first = (x2 - x1) ** 2
  second = (y2 - y1) ** 2
  third = (first + second) ** 0.5
  result = third
  return result

print("두 점의 거리 : ", distance(x1, y1, x2, y2))
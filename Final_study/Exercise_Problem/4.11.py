x1 = int(input('x1 좌표를 입력하세요 : '))
y1 = int(input('y1 좌표를 입력하세요 : '))
x2 = int(input('x2 좌표를 입력하세요 : '))
y2 = int(input('y2 좌표를 입력하세요 : '))

def area(x1, y1, x2, y2):
  result = 0;
  nArea = (x2 - x1) * (y2 - y1) / 2
  result = nArea
  return result

print('직각삼각형의 면적은 : ', area(x1, y1, x2, y2))
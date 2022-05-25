x = int(input('x값을 입력하세요 : '))
y = int(input('y값을 입력하세요 : '))

def square(x, y) :
  x1 = x ** 2
  y1 = y ** 2
  return x1, y1

x_sq, y_sq = square(x, y)
print('{} 제곱 = {}, {} 제곱 = {}'.format(x, x_sq, y, y_sq))


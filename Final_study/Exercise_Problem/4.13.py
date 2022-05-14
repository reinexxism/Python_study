# 정육면체 부피를 구하는 함수
def square(s):
  result = 0;
  nSquare = s * s * s
  result = nSquare
  return result

# 직육면체 부피를 구하는 함수
def rectangle(w, h, l):
  result = 0;
  nRectangle = w * h * l
  result = nRectangle
  return result

# 원뿔 부피를 구하는 함수
def cone(r, h):
  result = 0;
  nCone = (1/3) * 3.14 * r * r * h
  result = nCone
  return result

# 구 부피를 구하는 함수
def circle(r):
  result = 0;
  nCircle = (4/3) * 3.14 * r * r * r
  result = nCircle
  return result

# 원기둥 부피를 구하는 함수
def cylinder(r, h):
  result = 0;
  nCylinder = 3.14 * r * r * h
  result = nCylinder
  return result

print('모서리의 길이가 12인 정육면체 : ', square(12))
print('모서리의 길이가 20인 정육면체 : ', square(20))
print('가로, 세로, 길이가 각각 3, 5, 6인 직육면체 : ', rectangle(3, 5, 6))
print('반지름과 높이가 각각 20, 10인 원뿔 : ', cone(20, 10))
print('반지름이 15인 구', circle(15))
print('반지름과 높이가 각각 20, 10인 원기둥', cylinder(20, 10))
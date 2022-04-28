def get_root(a, b, c):
  r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
  r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
  return r1, r2

# 함수 호출시 1, 2, -8 인자를 사용함
#  result1, result2를 이용해서 결과 값을 반환 받는다
result1, result2 = get_root(a = 1, c = -8, b = 2)
print('해는', result1, '또는', result2)
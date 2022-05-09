a, b, c = map(int, input('정수를 입력하세요 : ').split())

def mean3(a, b, c):
  return (a + b + c) / 3

def max3(a, b, c):
  return max(a, b, c)

def min3(a, b, c):
  return min(a, b, c)

print(f'{a}, {b}, {c}의 평균값은', mean3(a, b, c))
print(f'{a}, {b}, {c}의 최댓값은 ', max3(a, b, c))
print(f'{a}, {b}, {c}의 최솟값은 ', min3(a, b, c))

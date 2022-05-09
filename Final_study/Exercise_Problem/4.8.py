a, b, c, d, e, f = map(int, input('여섯 개의 수를 입력하시오 : ').split())

def mean3(a, b, c):
  return (a + b + c) / 3

def max3(a, b, c):
  return max(a, b, c)

def min3(a, b, c):
  return min(a, b, c)

def mean6(a, b, c, d, e, f):
  result = 0;
  x = mean3(a, b, c)
  y = mean3(d, e, f)
  result = (x + y) / 2
  return result

def max6(a, b, c, d, e, f):
  x = max3(a, b, c)
  y = max3(d, e, f)
  if x > y:
    return x
  else:
    return y

def min6(a, b, c, d, e, f):
  x = min3(a, b, c)
  y = min3(d, e, f)
  if x > y:
    return y
  else:
    return x

print('평균값은 ', mean6(a, b, c, d, e, f))
print('최댓값은 ', max6(a, b, c, d, e, f))
print('최솟값은 ', min6(a, b, c, d, e, f))
# 복수로 주사위를 던졌을 때 특정값 이상을 얻을 확률 구하기

def tuple_sum(tup) :
  if isinstance(tup, int) :
    return tup
  else :
    accum = 0
    for element in tup :
      accum += tuple_sum(element)
  return accum

def product_set(set1, set2) :
  res = set()
  for i in set1 :
    for j in set2 :
      res = res | {(i, j)}
  return res

def exp(input_set, exponent) :
  res = input_set
  for _ in range(exponent-1) :
    res = product_set(res, input_set)
  return res

cases = {1, 2, 3, 4, 5, 6}
cases_2times = product_set(cases, cases)
cases_3times = product_set(cases, cases_2times)
print('주사위를 세 번 던져 발생할 수 있는 사건은 {} 가지 경우가 존재합니다.'.format(len(cases_3times)))
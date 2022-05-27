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

sum = [tuple_sum(tup) for tup in cases_3times]

count = 0
for i in sum :
  if i >= 10 :
    count += 1

print('주사위를 세 번 던져 나온 눈의 합이 10이상인 경우는 {} 가지입니다.'.format(count))
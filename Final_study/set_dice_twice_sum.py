# 주사위 두 번 던져 나오는 모든 경우에 대해 눈의 합 구하기
def product_set(set1, set2) :
  res = set()
  for i in set1 :
    for j in set2 :
      res = res | {(i, j)}
  return res

cases = {1, 2, 3, 4, 5, 6}
cases_2times = product_set(cases, cases)

# set : 중복되는 원소가 존재할 수 없음
sum_set = {sum(tup) for tup in cases_2times} 
print('sum_set = ', sum_set)

# list : 중복되는 원소가 존재할 수 있음
sum_list = [sum(tup) for tup in cases_2times]
print('sum_list = ', sum_list)
# 주사위를 세 번 던져 나오는 모든 수의 합
def tuple_sum(tup) : # tup 내의 모든 항목의 합을 구하는 function
  if isinstance(tup, int) : # 만약 tup가 int형이라면 tup를 반환
    return tup
  else :
    accum = 0
    for element in tup : # tup 내의 모든 항목을 조회함
      accum += tuple_sum(element) # 이 항목의 합을 구하기 위한 재귀적 호출
  return accum

def product_set(set1, set2) :
  res = set()
  for i in set1 :
    for j in set2 :
      res = res | {(i, j)} # 이중 for loop를 이용한 곱집합
  return res

cases = {1, 2, 3, 4, 5, 6}
cases_2times = product_set(cases, cases)
cases_3times = product_set(cases, cases_2times)

sums = [tuple_sum(tup) for tup in cases_3times] 
print(sums) # tup 내의 모든 항목의 합을 list형식으로 출력
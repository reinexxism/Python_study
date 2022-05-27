# 곱집합 함수를 이용한 집합의 세제곱 연산
def product_set(set1, set2) :
  res = set()
  for i in set1 :
    for j in set2 :
      res = res | {(i, j)} # 이중 for loop를 이용한 곱집합
  return res

def exp(input_set, exponent) :   # input_set에 대하여 거듭제곱을 수행하는 함수
  res = input_set                # res는 set으로 초기화 함
  for _ in range(exponent - 1) : # (exponent-1)만큼 반복해야 거듭제곱이 됨
    res = product_set(res, input_set)
  return res

A = {1, 3}
A3 = exp(A, 3) # 집합 A에 대하여 거듭제곱을 3회 수행함
print(A3)


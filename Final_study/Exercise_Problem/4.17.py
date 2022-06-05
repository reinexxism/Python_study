n1, n2 = map(int, input('숫자 두 개를 입력하세요 : ').split())

def sum_range(n1, n2) :
  nSum = 0
  for i in range(n1, n2+1) :
    nSum += i
  return nSum

print('{}에서 {}까지의 정수의 합 : {}'.format(n1, n2, sum_range(n1, n2)))
n = list(map(int, input('숫자들을 입력하세요 : ').split()))

def my_sort3(*nums) :
  list = []
  list.extend(n)
  list1 = sorted(list)
  return list1

print('결과 : ', my_sort3(n))
  
from xml.dom.minidom import TypeInfo


n = list(map(int, input('정수를 여러 개 입력하세요 : ').split()))

def mean_of_n(nums):
  result = 0;
  nSum = sum(nums)
  length = len(nums)
  result = nSum / length
  return result

def max_of_n(nums):
  result = max(nums)
  return result

def min_of_n(nums):
  result = min(nums)
  return result

print('평균값은 ', mean_of_n(n))
print('최댓값은 ', max_of_n(n))
print('최솟값은 ', min_of_n(n))

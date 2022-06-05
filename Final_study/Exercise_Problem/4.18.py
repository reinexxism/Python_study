# a, b, c의 최소공배수 <= a * b * c
a = int(input('범위의 시작 정수 : ')) # a = 1
b = int(input('범위의 마지막 정수 : ')) # b = 4

nList = list(range(a, b+1)) # nList = [1, 2, 3, 4]

maxLCM = 1
for i in nList: # nList의 요소들을 하나씩 i에 대입 / i = 1, 2, 3, 4
  maxLCM *= i  # maxLCM = 24 / maxLCM = 0으로 설정을 하면 어떠한 값을 곱해도 그대로 0이 되므로 오류

LCM = 0
for i in range(max(nList), maxLCM + 1): # 현재 범위 : range(4, 25)
  LCM = i 
  isLCM = True
  for j in nList:
    if (LCM % j != 0):
      isLCM = False
  if (isLCM == True): 
    break

print('{}에서 {}까지의 정수들의 최소 공배수는 : {}'.format(a, b, LCM))

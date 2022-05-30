import random as rd

print('이번 주의 추천 로또번호')
for i in range(6) : 
  lotto_list = list(range(1, 46))
  rd.shuffle(lotto_list)
  lotto_list = lotto_list[:6]
  lotto_list.sort()
  print(lotto_list)
  


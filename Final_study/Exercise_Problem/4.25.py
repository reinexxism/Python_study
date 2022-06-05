import re


s1 = 'Kang Young Min'
s2 = ' Kang Young-Min'
s3 = 'Park Dong Min'
s4 = ' Park Dong-Yun'

L = [s1, s2, s3, s4]
for i in range(4) :
  result = L[i].replace(' ', '')
  result = result.replace('-', '')
  result = result.upper()
  print('{}은(는) {}(으)로 수정됨'.format(L[i], result))
  L[i] = result
  
for i in L : 
  N = 0
  for j in i :
    if j == 'N' :
      N += 1
  print('{} : {}개의 N이 나타남'.format(i, N))
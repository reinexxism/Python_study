n = 7
for i in range(n):   #외부 for loop는 7번 수행
  st = (' ' * n)
  for j in range(i):   #내부 for loop는 i번 수행
    st = (' ' * (n -i)) 
  print(st + '#')

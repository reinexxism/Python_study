n = int(input('정수를 입력하세요 : '))
for i in range(n):    #외부 for loop는 n번 수행, i는 (n-1)까지 증가
  st=''
  for j in range(i):  #내부 for loop는 i번 수행
    st = st + ' '     #공백을 1개 추가
  print(st + '#')     
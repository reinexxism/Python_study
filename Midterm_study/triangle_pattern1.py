n = 5
for i in range(n):  # i는 0,1,2,3,4까지 증가함
  for j in range(n-(i+1)):  # j는 4,3,2,1,0이 된다. // 공백을 출력한다.
    print(' ', end='')
  for j in range(2 * i + 1):   #'+'를 출력한다.
    print('+', end='')
  print()

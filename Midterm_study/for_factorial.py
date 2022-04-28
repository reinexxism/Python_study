n = int(input('수를 입력하세요 : '))
fact = 1                    # factorial 계산 시에는 초기값을 0이 아닌 1로 할당
for i in range(1, n+1):     # i 가 자동으로 n까지 루프
  fact = fact * i

print('{}! = {}'.format(n, fact))
n = list(map(int, input('10개의 수를 입력하세요 : ').split()))

print('합 : {}'.format(sum(n)))
n_avg = sum(n)/len(n)
print('평균 : {}'.format(n_avg))
n_sigma = 0
for i in n :
  n_sigma += (i - n_avg) ** 2
print('표준 편차 : {:.2f}'.format((n_sigma / len(n)) ** 0.5))
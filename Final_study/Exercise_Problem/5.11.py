n = list(map(int, input('5개의 수를 입력하세요 : ').split()))

print('합 = {}'.format(sum(n)))
print('평균 = {}'.format(sum(n)/len(n)))
print('최댓값 = {}'.format(max(n)))
print('최솟값 = {}'.format(min(n)))
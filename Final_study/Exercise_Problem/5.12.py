n = int(input('n을 입력하세요 : '))
n_list = list(map(int, input('{}개의 수를 입력하세요 : '.format(n)).split()))

print('합 : {}'.format(sum(n_list)))
print('평균 : {}'.format(sum(n_list)/len(n_list)))
print('최댓값 : {}'.format(max(n_list)))
print('최솟값 : {}'.format(min(n_list)))


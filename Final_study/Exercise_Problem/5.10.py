n_list = [10, 20, 30, 50, 60]
print('리스트 원소들 : ', n_list)

v_min = 999999
for i in n_list :
  if i < v_min :
    v_min = i
print('리스트의 원소들 중 최솟값 : ', v_min)
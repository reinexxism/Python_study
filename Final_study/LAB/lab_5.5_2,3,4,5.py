n_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(n_list)

n_list.insert(0, 0) # list안에 원소를 삽입하는 method
print(n_list)

n_list.reverse() # list 안의 원소들을 역순으로 배열하는 method
print(n_list)

print('마지막 원소 = ', n_list.pop()) # list가장 마지막의 원소를 제거하고 그 값을 반환하는 method
print('n_list = ', n_list)
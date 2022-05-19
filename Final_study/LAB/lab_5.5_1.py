a_list = [1, 2, 3]
b_list = [10, 20, 30]

a_list.append(b_list) # append() method는 요소를 추가하는 method
print(a_list)

a_list = [1, 2, 3]
b_list = [10, 20, 30]

a_list.extend(b_list) # extend() method는 리스트 자체를 추가하는 method (확장의 개념)
print(a_list)

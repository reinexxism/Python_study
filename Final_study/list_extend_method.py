list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

list1.extend(list2) # list2의 요소를 list1에 추가하는 method
print(list1)

list1.extend('d') # 'd'원소를 list1에 추가하는 method
print(list1)
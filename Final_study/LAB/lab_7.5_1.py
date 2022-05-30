import random as rd

# list1 = rd.randrange(0, 101, 5)
# print(list1)
# print('0에서 100이하의 정수 중에서 5의 배수')

list1 = list(range(0, 101, 5))
list2 = rd.sample(list1, 3)
print(list2)
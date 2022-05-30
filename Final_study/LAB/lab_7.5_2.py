import random as rd

number_list = list(range(1, 11))
number_list2 = rd.sample(number_list, 3)
print('1에서 10 사이의 임의의 정수 : ', number_list2)
from re import T


# tuple의 항목 값을 list를 이용하여 변환
t_fruits = ('apple', 'orange', 'water melon')
print('변경 전 :', t_fruits)

t_fruits = list(t_fruits) # tuple을 list로 변환
t_fruits[1] = 'kiwi' # list의 두 번째 항목 값을 'kiwi'로 변경함
t_fruits = tuple(t_fruits) # list를 tuple로 변환

print('변경 후 : ', t_fruits)
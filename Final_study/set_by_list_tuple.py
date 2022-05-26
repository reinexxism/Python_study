# list와 tuple, literal로부터 집합 만들기

# list로부터 set 만들기
days_list = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
days_set = set(days_list)
print(days_set)

# tuple로부터 set 만들기
fruits_tuple = ('apple', 'orange', 'water melon')
fruits_set = set(fruits_tuple)
print(fruits_set)

# literal로부터 set 만들기
h_str = 'hello'
h_set = set(h_str)
print(h_set) # set에서는 literal 'l'의 중복을 허용하지 않음

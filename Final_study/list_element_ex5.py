# lambda함수와 map을 이용하여 리스트 요소들을 조작하는 method

list1 = [10, 20, 30, 40, 50]
list1 = list(map(lambda x: x * 10, list1))

print(list1)
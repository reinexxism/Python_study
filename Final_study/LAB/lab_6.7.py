person = ('홍길동', 2019001, 179) # 'person' tuple
person2 = list(person) # 'person' tuple을 list 형태로 변환하여 person2 변수에 할당
person2[1] = 2020003 # 'person2' list의 1번째 index value를 변경
person3 = tuple(person2) # 'person2' list를 tuple 형태로 변환하여 person3 변수에 할당
print('학번 변동 후 person = ', person3) 
# dictionary의 항목 삭제와 dic[1] 항목의 변화 여부
dic = {0:11, 1:22, 2:33, 3:44, 4:55}

print('pop(0) 이전 : ', dic.items()) # dictionary의 [key:value] 튜플쌍을 반환하는 items() fuction으로 출력
print('pop(0) 이전 dic[1] = ', dic[1])

dic.pop(0) # key 0을 이용하여 (0, 11) 항목을 제거함

print('pop(0) 이후 : ', dic.items())
print('pop(0) 이후 dic[1] = ', dic[1]) # dic[1]이 참조하는 값이 변하지 않음

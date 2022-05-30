# random module을 활용한 섞기와 고르기
import random as rd
numlist = [10, 20 , 30, 40, 50]

# rd.shuffle(seq) : 주어진 seq list의 요소를 랜덤하게 섞는다.
a = rd.shuffle(numlist)
print(numlist)

# rd.choice(seg) : seq 시퀀스 내의 임의의 요소를 선택한다.
b = rd.choice(numlist)
print(b)

# rd.sample(seq) : 지정된 개수의 요소를 임의로 선택한다.
c = rd.sample(numlist, 3)
print(c)

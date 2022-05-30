# random module을 활용한 값 생성
import random as rd

# rd.random() : 0에서 1 사이의 실수를 생성하고 반환
# 매번 다른 실수를 반환
a = rd.random()
print(a)

# rd.randrange() : 지정된 범위 내의 정수를 반환
# 이상 ~ 미만
b = rd.randrange(1, 7)
print(b)

# 1 이상 10 미만 정수 중 2의 배수를 반환
c = rd.randrange(0, 10, 2)
print(c)

# rd.randint() : a <= N <= b 사이의 랜덤 정수 N을 생성하고 반환
# 이상 ~ 이하
d = rd.randint(1, 10)
print(d)
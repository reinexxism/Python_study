# random module을 이용한 로또 번호 만들기2
import random as rd

lotto_list = list(range(1, 46))
lotto_list = rd.sample(lotto_list, 6) # 임의의 값 6개를 추출(샘플링 활용)
lotto_list.sort()
print('이번 주의 추천 로또번호 : ', lotto_list)
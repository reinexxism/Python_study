import random as rd

lotto_list = list(range(1, 46))
lotto_list = rd.sample(lotto_list, 6)
lotto_list.sort()

bonus_num = list(range(1,46))
bonus_num = rd.sample(bonus_num, 1)

print('이번 주의 추천 로또번호 + 보너스 ')
print(lotto_list, '+', bonus_num)

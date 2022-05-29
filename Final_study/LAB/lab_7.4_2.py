# 일반각도 0에서 180도를 10도 단위로 출력
import math as m

for i in range(0, 190, 10) :
  print('{} degree = {:.3f} radian'.format(i, m.radians(i)))
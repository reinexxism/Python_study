# color(), begin_fill(), end_fill()을 이용한 색상 사각형 그리기
import turtle as t

t.color('blue') # 색상으로 파란색을 선택
t.begin_fill()  # 내부를 채움
for i in range(4) :
  t.forward(100)
  t.left(90)
t.end_fill()    # 사각형 내부를 파란색으로 채워서 그리기

t.done()
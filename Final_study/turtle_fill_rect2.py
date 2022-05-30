# 여러 개의 사각형 그리기
import turtle as t

t.color('blue') 
t.begin_fill()
for i in range(4) :
  t.forward(100)
  t.left(90)
t.end_fill() # 첫번째 사각형의 내부 : 파란색

t.setheading(90)
t.color('red')
t.begin_fill()
for i in range(4) :
  t.forward(100)
  t.left(90)
t.end_fill() # 두번째 사각형의 내부 : 빨간색

t.done()
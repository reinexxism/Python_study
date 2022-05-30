# for 반복문과 forward(), left() method를 사용한 사각형 그리기
import turtle as t

t.shape("turtle")

for i in range(4) :
  t.forward(100)
  t.left(90)

t.done()
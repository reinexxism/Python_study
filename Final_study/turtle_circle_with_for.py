# forward(), left() 명령을 사용한 원 그리기
import turtle as t

t.shape("turtle")
n = 100
length = 5
for i in range(n) :
  t.left(360 / n)
  t.forward(length)

t.done()
# circle 명령을 이용한 여러 개의 원 그리기
import turtle as t

t.shape("turtle")

# left circle
t.setheading(90)
for i in range(1, 11) :
  t.circle(10 * i)

# right circle
t.setheading(270)
for i in range(1, 11) :
  t.circle(10 * i)

t.done()
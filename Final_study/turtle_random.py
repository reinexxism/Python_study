# 터틀 그래픽의 랜덤 플로팅
import turtle as t
import random as rd

t.shape("circle")
d = 300
t.penup()
for i in range(40) :
  x = rd.randint(-d, d)
  y = rd.randint(-d, d)
  t.goto(x, y)
  t.stamp()
t.done()

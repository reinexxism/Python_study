import turtle as t
import random as rd

colors = ['red', 'green', 'blue', 'orange']
d = 300
t.shape("turtle")
t.shapesize(2, 2)
t.penup()
for i in range(40) :
  x = rd.randint(-d, d)
  y = rd.randint(-d, d)
  t.goto(x, y)
  t.color(colors[i % 4])
  t.stamp()

t.done()

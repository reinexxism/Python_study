import turtle as t

t.shape("turtle")
for i in range(100, 400, 100) :
  for j in range(3) :
    t.forward(i)
    t.left(120)

t.done()
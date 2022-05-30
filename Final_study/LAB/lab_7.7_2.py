import turtle as t

t.shape("turtle")
for i in range(3) : # 한 변의 길이가 100px인 정삼각형
  t.forward(100)
  t.left(120)

for i in range(3) : # 한 변의 길이가 200px인 정삼각형
  t.forward(200)
  t.left(120)

t.done()
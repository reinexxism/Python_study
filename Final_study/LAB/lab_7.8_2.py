import turtle as t
colors = ['blue', 'red', 'yellow', 'green']

def draw_rect(num) :
  t.color(colors[num % 4])
  t.setheading(num * 90)
  t.begin_fill()
  for i in range(4) :
    t.forward(100)
    t.left(90)
  t.end_fill()

for i in range(4) :
  draw_rect(i)
t.done()
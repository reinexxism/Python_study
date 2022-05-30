import turtle as t

# first rectangle : inside 'blue' color
# setheading : 0
t.color('blue')
t.begin_fill()
for i in range(4) :
  t.forward(100)
  t.left(90)
t.end_fill()

# second rectangle : inside 'red' color
# setheading : 90
t.setheading(90)
t.color('red')
t.begin_fill()
for i in range(4) :
  t.forward(100)
  t.left(90)
t.end_fill()

# third rectangle : inside 'yellow' color
# setheading : 180
t.setheading(180)
t.color('yellow')
t.begin_fill()
for i in range(4) :
  t.forward(100)
  t.left(90)
t.end_fill()

# fourth rectangle : inside 'green' color
# setheading : 270
t.setheading(270)
t.color('green')
t.begin_fill()
for i in range(4) :
  t.forward(100)
  t.left(90)
t.end_fill()

t.done()


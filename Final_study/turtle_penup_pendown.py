# goto(), penup(), pendown() method
import turtle as t

t.goto(80, 100) # 1 : (80, 100)까지 선을 그린다.
t.penup()       # 2: 펜을 든다 (선을 그리지 않고 해당 좌표로 이동)
t.goto(0, 100)  # 3: 펜을 해당 좌표(0, 100)로 이동
t.pendown()     # 4 : 펜을 내린다 (선을 그리면서 다음 좌표로 이동)
t.goto(80, 0)   # 5 : (80, 0)까지 선을 그린다.

t.done()
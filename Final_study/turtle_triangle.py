# forward() 명령과 left() 명령을 이용한 turtle 삼각형 그리기
import turtle as t

t.shape("turtle")
t.forward(100)   # turtle을 heading 방향으로 100px 이동
t.left(120)      # turtle의 heading 방향을 120도 회전
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)

t.done()
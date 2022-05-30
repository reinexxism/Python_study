# for문을 사용한 turtle 삼각형 그리기
import turtle as t

t.shape("turtle")
for i in range(3) :  # 아래의 기능을 세 번 반복
  t.forward(100)     # turtle을 heading 방향으로 100px 이동
  t.left(120)        # turtle의 heading 방향을 120도 회전

t.done()
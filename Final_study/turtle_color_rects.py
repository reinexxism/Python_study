# pencolor() method를 이용한 패턴 만들기
import turtle as t

colors = ['red', 'green', 'orange', 'blue'] # colors라는 list를 생성
t.bgcolor("black") # 배경색상을 변경
t.speed(0) # 패턴 그리기 속도를 향상
for i in range(200) :
  t.pencolor(colors[i % 4]) # colors list의 항목이 교대로 나타나도록 설정하여 색상을 인덱싱
  t.forward(i)
  t.left(93)

t.done()


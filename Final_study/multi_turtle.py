# 하나 이상의 터틀 객체를 생성하여 나타내기
import turtle as t

t1 = t.Turtle()     # Turtle 객체를 하나 생성하고 t1이 참조함
t1.shape("circle")  # t1 객체의 형태를 circle로 지정
t1.goto(100, 0)     # t1 객체를 (100, 0) 위치로 이동

t2 = t.Turtle()     # 또 다른 Turtle 객체를 생성하고 t2가 참조함
t2.shape("square")  # t2 객체의 형태를 square로 지정
t2.goto(-100, 100)  # t2 객체를 (-100, 100) 위치로 이동

t.done()


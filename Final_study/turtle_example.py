# turtle graphic의 setup(), forward(), left(), done() method
import turtle as t

t.setup(width = 400, height = 400)
for i in range(200) :
  t.forward(i)
  t.left(93)

t.done()
# done() 명령어 : 이 프로그램을 event loop로 진입시키는 기능
# event : 마우스나 키보드와 같은 사용자 입력이나 시간의 진행과 같은 사건의 총칭
# event driven programming(이벤트 기반 프로그램) : 이러한 event에 의해서 실행되는 프로그램
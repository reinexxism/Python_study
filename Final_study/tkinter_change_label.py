# Tkinter를 이용한 간단한 실습 코드
# Btn과 Label을 가지고 Btn을 클릭할 때마다 서로 다른 Label을 표시하는 프로그램 만들기
from tkinter import *

def change_label() :
  if label.cget("text") == '헬로 파이썬' :
    label.config(text = '안녕 파이썬')
    label.config(bg = 'cyan')
  else :
    label.config(text = '헬로 파이썬')
    label.config(bg = 'yellow')

window = Tk()
label = Label(window, text = '헬로 파이썬', bg = 'yellow')
label.pack()
btn = Button(window, text = '클릭하면 문자가 변경됨', fg = 'blue', command = change_label)
btn.pack()

window.mainloop()

# 파일 열기와 읽기, 파일 닫기의 표현
f = open('hello.txt', 'r')
s = f.read()
print(s)
f.close()
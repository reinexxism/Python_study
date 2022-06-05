# 사용자로부터 입력받은 파일을 번호를 붙여서 출력하기
fname = input('입력할 파일의 이름 : ')
f = open(fname, 'r')
n = 1
l = f.readline()
while l :  # 읽어들일 줄이 있을 때까지 반복수행 (없으면 수행을 중단)
  print('{:3d}: {}'.format(n, l), end='') # 줄 번호와 내용을 출력
  n += 1 # 줄 번호를 1씩 증가시킴
  l = f.readline() # 다음 줄을 읽어온다.

f.close()
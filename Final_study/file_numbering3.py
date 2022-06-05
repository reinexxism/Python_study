# try-except문을 사용한 파일 입출력
import sys

fname = input('입력할 파일의 이름 :')
try :
  f = open(fname, 'r', encoding='UTF8')
except IOError :
  print('Could not read file :', fname)
  sys.exit()
except :
  print('Unexpected error : ', sys.exc_info()[0])
  sys.exit()

n = 1
l = f.readline()
while l :
  print('{:3d}: {}'.format(n, l), end='')
  n += 1
  l = f.readline()
f.close()
import sys
file = input('입력할 파일의 이름 : ')

try : 
  f = open(file, 'r', encoding = 'UTF8')
except IOError :
  print('Could not read file : ', file)
  sys.exit()
except :
  print('Unexpected error : ', sys.exc_info()[0])
  sys.exit()
else : 
  for x in f.read() :
    y = x.upper()
    file2 = open(file, 'a')
    file2.write(y)


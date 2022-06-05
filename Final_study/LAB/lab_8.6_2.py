import sys
file = input('파일 이름을 입력하세요 : ')

try : 
  f = open(file, 'r', encoding = 'UTF8')
# except IOError :
#   print('Could not read file : ', file)
except :
  print('Unexpected error : ', sys.exc_info([0]))
else :
  lines = f.readlines()
  for line in reversed(lines) :
    print(line)

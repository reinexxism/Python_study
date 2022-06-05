# readline() method를 이용한 줄 단위 읽기와 출력하기
f = open('foo.txt', 'w')
f.write('AAA\n')
f.write('BBB\n')
f.write('CCC\n')
f.close()

f1 = open('foo.txt', 'r')
s = f1.readline()   # 파일의 첫 번째 줄 'AAA'를 읽어온다.
print(s, end='')
s = f1.readline()   # 파일의 두 번째 줄 'BBB'를 읽어온다.
print(s, end='')
# readline() method와 rstrip()을 이용한 줄 단위 읽기와 출력
f = open('foo.txt', 'r')
s = f.readline().rstrip() # 'AAA'줄을 읽고 오른쪽에 있는 모든 공백문자를 지움
print(s)
s = f.readline().rstrip() # 'BBB'줄을 읽고 오른쪽에 있는 모든 공백문자를 지움
print(s)
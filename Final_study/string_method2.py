# 문자열 사이에 ','삽입 -> join() method
a = ','.join('ABCD')
print(a)

# 오른쪽 공백 지우기 -> rstrip() method
b = '   hello   '.rstrip()
print(b)

# 왼쪽 공백 지우기 -> lstrip() method
c = '   hello   '.lstrip()
print(c)

# 공백 지우기 -> strip() method
d = '   hello   '.strip()
print(d)

# 문자열 교환 -> replace() method
e = 'Long live the king!'
f = e.replace('king', 'Queen')
print(f)

# 타이틀 문자열로 변환 -> title() method
g = 'Long live the king!'
h = g.title()
print(h)

# 첫 문자만 대문자로 변환 -> capitalize() method
i = 'Long live the king!'
j = i.capitalize()
print(j)

# :를 구분자로 하여 k 문자를 리스트로 분리 -> split(:) method
k = 'X:Y:Z'
l = k.split(':')
print(l)

# + 연산자를 이용하여 m 문자를 연결 -> '+'
m = 'Hello' + 'Python'
print(m)

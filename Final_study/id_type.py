# id()함수는 객체의 식별값을 정수형으로 반환하는 함수
a_str = "Hello Python!"
b = id(a_str)
print(b)

n = 300
c = id(n)
print(c)

# type()함수는 객체의 자료형을 반환하는 함수
d = type(123)
print(d) # 숫자형 'int'

e = type('Hello String!')
print(e) # 문자형 'str'

f = type(120.3)
print(f) # 실수형 'float'

g = type([100, 300, 600])
print(g) # 배열 'list'

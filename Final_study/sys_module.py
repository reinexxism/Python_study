# sys module을 이용한 파이썬 버전과 경로, 저작권
import sys

# prefix 속성 : 파이썬이 설치된 경로
a = sys.prefix
print(a)

# version 속성 : 파이썬 인터프리터의 현재 버전
b = sys.version
print(b)

# copyright 속성 : 파이썬의 저작권에 대한 내용
c = sys.copyright
print(c)

# path 속성 : 모듈을 찾을 때 참조하는 경로
d = sys.path
print(d)
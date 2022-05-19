a_list = [10, 20, 30, 40, 50, 60, 70, 80]

a = a_list[1:5]
print(a)

b = a_list[0:1]
print(b)

c = a_list[0:2]
print(c)

d = a_list[0:5]
print(d)

e = a_list[1:]
print(e)

f = a_list[:5]
print(f)

# 1. slicing을 할 때 범위를 지정하는 방법 : 인덱스 사이에 ':'을 지정
# 2. slicing을 할 때 시작 인덱스와 끝 인덱스는 생략이 가능
# 3. slicing을 할 때 콜론(:)뒤에 명시한 마지막 인덱스는 슬라이싱 리스트에 포함되지 않음

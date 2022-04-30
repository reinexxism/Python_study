# 절대값을 반환하는 함수 -> abs() function
a = abs(-100)
print(a)

# 여러 원소들 중 최솟값을 반환하는 함수 -> min() function
b = min(200, 100, 300, 400)
print(b)

# 여러 원소들 중 최댓값을 반환하는 함수 -> max() function
c = max(200, 100, 300, 400)
print(c)

# 문자열의 길이를 반환하는 함수 -> len() function
d = 'FOO'
e = len(d)
print(e)

# 문자열을 수치값과 연산자로 변환하여 평가하는 함수 -> eval() function
f = eval('100+200+300')
print(f)

# 문자열을 정렬하는 함수 -> sorted() function / reverse = True 사용시 반대로 반환
g = sorted('EABFD')
print(g)

h = [200, 100, 300, 400]
i = sorted(h)
print(i)

j = sorted(h, reverse = True)
print(j)
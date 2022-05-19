from calendar import c


fruits = ['banana', 'orange', 'apple', 'kiwi']

a = min(fruits) # 영어사전 순서로 가장 앞에 있는 단어를 반환
print(a)

b = max(fruits) # 영어사전 순서로 가장 뒤에 있는 단어를 반환
print(b)


k_fruits = ['사과', '오렌지', '포도', '바나나'] # min()과 max()는 한글 문자열을 요소로 가지는 리스트에도 적용 가능

c = min(k_fruits)
print(c)

d = max(k_fruits)
print(d)
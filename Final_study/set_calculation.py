s1 = {1, 2, 3, 4, 5, 6}
s2 = {4, 5, 6, 7, 8, 9}

# 합집합을 구함 : 두 집합의 요소를 모두 포함 
# '|' = .union()
print(s1 | s2)
print(s1.union(s2))

# 교집합을 구함 : 두 집합의 공통요소만을 포함
# '&' = .intersection()
print(s1 & s2)
print(s1.intersection(s2))

# 차집합을 구함
# '-' = .difference()
print(s1 - s2)
print(s1.difference(s2))

# 대칭 차집합을 구함 : 합집합에서 교집합을 제외한 요소를 포함
# '^' = .symmetric_difference()
print(s1 ^ s2)
print(s1.symmetric_difference(s2))
s1 = {1, 2, 3, 4, 5}
s2 = {1, 2, 3} # s1의 부분집합임(True)
s3 = {1, 2, 6} # s1의 부분집합이 아님(False)

# s2가 s1의 부분집합인지를 묻는 method
print(s2.issubset(s1))

# s3가 s1의 부분집합인지를 묻는 method
print(s3.issubset(s1))

# s1이 s2의 상위집합인지를 묻는 method
print(s1.issuperset(s2))

# s1이 s3의 상위집합인지를 묻는 method
print(s1.issuperset(s3))



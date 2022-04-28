from unittest import result


def multiplies(n, m):
  for i in range(1, m+1):
    result = n * i
  return result

r1, r2, r3, r4 = multiplies(3, 4)
print(r1, r2, r3, r4)
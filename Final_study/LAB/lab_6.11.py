def product_set(set1, set2) :
  res = set()
  for i in set1 :
    for j in set2 :
      res = res | {(i, j)}
  return res

A = {1, 2}
B = {'A', 'B', 'C'}

print(product_set(A, B))
print(product_set(B, A))
print(product_set(A, A))
print(product_set(B, B))

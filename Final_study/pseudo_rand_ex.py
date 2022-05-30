def pseudo_rand(x) :
  a = 1103515245
  b = 12345
  m = 2 ** 31
  new_x = (a * x + b) % m
  return new_x

x = pseudo_rand(101)
print(x)
y = pseudo_rand(100)
print(y)
def func(shape, width = 1, height = 1, radius = 1):
  if shape == 0 :  #shape값이 0이면 rectangle_area값을 반환
    return width * height
  if shape == 1 :  #shape값이 1이면 circle_area값을 반환
    return 3.14 * radius ** 2

print('rect area = ', func(0, width = 10, height = 2))
print('circle area = ', func(1, radius = 5))
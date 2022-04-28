def circle_area_circum(radius):
  area = 3.14 * radius * radius
  circum = 3.14 * 2 * radius
  return area, circum

radius = 10
area, circum = circle_area_circum(radius)
print('반지름 ', radius, '인 원의 면적은 ', area, ', 원의 둘레는 ', circum)

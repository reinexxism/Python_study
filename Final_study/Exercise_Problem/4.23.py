from xml.etree.ElementTree import PI


def area_and_circumference(r) :
  area = r * r * 3.14
  circumference = 2 * r * 3.14
  return area, circumference

while True :
  r = int(input('반지름을 입력하시오 : '))
  if (r <= 0) :
    print('프로그램을 종료합니다.')
    break
  rTuple = area_and_circumference(r)
  print('넓이 : {:7.3f}, 둘레 : {:7.3f}'.format(rTuple[0], rTuple[1]))

print('세 수를 입력하세요 : ')
s1 = int(input(''))
s2 = int(input(''))
s3 = int(input(''))

def sort3(num1, num2, num3) :
  list = []
  list.append(num1)
  list.append(num2)
  list.append(num3)
  list1 = sorted(list)
  print('정렬된 리스트는 다음과 같습니다 :  {} {} {}'.format(list1[0], list1[1], list1[2]))

sort3(s1, s2, s3)

a = [1, 2, 3, 4, 5]
print('a = ', list(a))

try :
  num = int(input('a의 요소를 하나 선택하시오 : '))
except ValueError :
  print('오류 : 입력 값이 정수나 실수가 아님')
else : 
  if (num == 1) :
    print('{} 은(는) 첫 번째 요소입니다.'.format(num))
  elif (num == 2) :
    print('{} 은(는) 두 번째 요소입니다.'.format(num))
  elif (num == 3) :
    print('{} 은(는) 세 번째 요소입니다.'.format(num))
  elif (num == 4) :
    print('{} 은(는) 네 번째 요소입니다.'.format(num))
  elif (num == 5) :
    print('{} 은(는) 다섯 번째 요소입니다.'.format(num))
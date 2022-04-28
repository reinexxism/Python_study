num = int(input('정수를 입력하세요 : '))

if num < 0:
  print(num, '은(는) 음수입니다.')
else:
  print(num, '은(는) 양수입니다.')
  if num % 2 == 0:    #짝수, 홀수는 음수가 아닐때만 판별가능.
    print(num, '은(는) 짝수입니다.')
  else:
    print(num, '은(는) 홀수입니다.')
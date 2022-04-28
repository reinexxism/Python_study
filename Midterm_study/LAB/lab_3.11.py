n1, n2, n3 = map(int,input('복권 번호를 입력하시오 : ').split())

if (n1 == 2 or n1 == 3 or n1 == 9) and (n2 == 2 or n2 == 3 or n2 == 9) and (n3 == 2 or n3 == 3 or n3 == 9):
  print('상금 1억원')
elif (n1 != 2 or n1 != 3 or n1 != 9) and (n2 ==2 or n2 == 3 or n2 == 9) and (n3 == 2 or n3 == 3 or n3 ==9):
  print('상금 1천만원')
elif (n1 == 2 or n1 == 3 or n1 == 9) and (n2 !=2 or n2 != 3 or n2 != 9) and (n3 == 2 or n3 == 3 or n3 ==9):
  print('상금 1천만원')
elif (n1 == 2 or n1 == 3 or n1 == 9) and (n2 ==2 or n2 == 3 or n2 == 9) and (n3 != 2 or n3 != 3 or n3 !=9):
  print('상금 1천만원')
elif (n1 == 2 or n1 == 3 or n1 == 9) or (n2 == 2 or n2 == 3 or n2 == 9) or (n3 == 2 or n3 == 3 or n3 == 9):
  print('상금 1만원') 
else:
  print('다음 기회에...') 
  
  
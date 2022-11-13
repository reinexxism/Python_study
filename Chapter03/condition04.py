number = input("정수를 입력해주세요 : ")
number = int(number)

if number % 2 == 0 :
  print("{}은(는) 짝수입니다.".format(number)) # if condition is True;
else :
  print("{}은(는) 홀수입니다.".format(number)) # if condition is False;
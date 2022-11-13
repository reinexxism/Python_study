number = input("정수를 입력해주세요 : ")
number = int(number)

# Condition1
if number % 2 == 0 :
  print("{}은(는) 짝수입니다.".format(number))

# Condition2
if number % 2 == 1 :
  print("{}은(는) 홀수입니다.".format(number))
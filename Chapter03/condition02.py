number = input("정수를 입력해주세요 : ")
last_character = number[-1]

# Condition1
if last_character in "02468" :
  print("{}은(는) 짝수입니다.".format(number))

# Condition2
if last_character in "13579" :
  print("{}은(는) 홀수입니다.".format(number))
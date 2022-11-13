# Input
number = input("정수를 입력하세요 : ")

last_character = number[-1]
last_number = int(last_character)

if last_number == 0 or last_number == 2 or last_number == 4 or last_number == 6 or last_number == 8 :
  print("{}는(은) 짝수입니다.".format(number))
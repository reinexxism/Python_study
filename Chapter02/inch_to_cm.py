# 1. Input
raw_input = input("inch 단위의 숫자를 입력해주세요 : ")

# 2. Convert
inch = int(raw_input)
cm = inch * 2.54

# Output
print(inch, "inch는 cm 단위로", cm, "cm입니다.")

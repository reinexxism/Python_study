score = float(input("학점을 입력해주세요 : "))

if score == 4.5 :
  print("당신은 신입니다.")
elif 4.2 <= score :
  print("당신은 교수님의 사랑입니다.")
elif 3.5 <= score :
  print("당신은 현 체제의 수호자입니다.")
elif 2.8 <= score :
  print("당신은 일반인입니다.")
elif 2.3 <= score :
  print("당신은 일탈을 꿈꾸는 소시민입니다.")
elif 1.75 <= score :
  print("당신은 오락문화의 선구자입니다.")
elif 1.0 <= score :
  print("당신은 불가촉천민입니다.")
elif 0.5 <= score :
  print("당신은 자벌레입니다.")
elif 0 < score :
  print("당신은 플랑크톤입니다.")
else :
  print("당신은 시대를 앞서가는 혁명의 씨앗입니다.")
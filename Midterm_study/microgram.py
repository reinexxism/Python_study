micro = int(input('미세먼지 농도를 입력하세요(단위 : microgram/m^3) : ' ))

if micro >= 76:
  print('매우 나쁨')
elif (micro < 76 and micro >=36):
  print('나쁨')
elif (micro < 36 and micro >= 16):
  print('보통')
else:
  print('좋음')

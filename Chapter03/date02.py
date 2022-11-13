import datetime
now = datetime.datetime.now()

# Condition1
if now.hour > 12 :
  print("현재 시각은 {}시로 오후입니다.".format(now.hour))

# Condition2
if now.hour < 12 :
  print("현재 시각은 {}시로 오전입니다.".format(now.hour))
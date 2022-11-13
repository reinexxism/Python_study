import datetime
now = datetime.datetime.now()

# Condition1
if 3 <= now.month <= 5 :
  print("이번 달은 {}월로 봄입니다.".format(now.month))

# Condition2
if 6 <= now.month <= 8 :
  print("이번 달은 {}월로 여름입니다.".format(now.month))

# Condition3
if 9 <= now.month <= 11 :
  print("이번 달은 {}월로 가을입니다.".format(now.month))

# Condition4
if 12 <= now.month <= 2 :
  prinf("이번 달은 {}월로 겨울입니다.".format(now.month))
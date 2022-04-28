score = int(input('점수를 입력하세요 : '))

if score >= 90:
  grade = 'A'
else:
  if score >= 80:
    grade = 'B'
  else:
    if score >= 70:
      grade ='C'
    else:
      if score >= 60:
        grade = 'D'
      else:
        grade = 'F'

print('당신의 등급은 : ', grade)
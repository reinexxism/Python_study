def greet(*names):
  for name in names:
    print('안녕하세요', name, '씨')

greet('홍길동', '양만춘', '이순신')  # 인자가 3개인 경우
greet('James', 'Thomas')  # 인자가 2개인 경우
# pseudo_rand() function을 이용한 연속적인 난수 만들기
def pseudo_rand(x) :
  new_x = (1103515245 * x + 12345) % ( 2 ** 31)
  return new_x

x = 12234 # 씨앗(seed)이 되는 초기 번호(초기에 난수를 생성하기 위한 값)
for _ in range(5):
  x = pseudo_rand(x)
  print(x)
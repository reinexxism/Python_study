# 소수를 담을 리스트 초기화
primes = []

for n in range(2, 101):
  # 일단 n이 소수라는 전제하에 진행
  is_prime = True
  for num in range(2, n):  # 2~(n-1) 사이의 수 num에 대하여(2부터 시작, n-1까지 종료)
    if n % num == 0:       # 이 수 중에서 n의 약수가 있으면
      is_prime = False     # 소수가 아님

  if is_prime:             # 소수일 경우 primes라는 리스트에 추가한다.
    primes.append(n)       # append() 메소드는 리스트에 n을 추가한다.

print(primes)
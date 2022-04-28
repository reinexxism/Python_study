st = 'Programming'

#자음이 나타날때만 출력하는 기능
for ch in st:
  if ch in ['a', 'e', 'i', 'o', 'u']:
    continue  #모음일 경우 아래 출력을 건너뛴다.
  print(ch)

print('The end')
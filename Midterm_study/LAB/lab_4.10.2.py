def sum_nums(*numbers):
  sum = 0
  nArgs = len(numbers)
  avg = 0

  for n in numbers:
    sum += n
  avg = sum / nArgs

  print(nArgs, '개의 인자 ', numbers)
  print('합계 : ', sum, ', 평균 : ', avg)

sum_nums(10, 20, 30, 40, 50) 
def sum_nums(*numbers):
  sum = 0
  nArgs = len(numbers)
  avg = 0
  
  for n in numbers:
    sum += n
  avg = sum / nArgs

  return nArgs, numbers, sum, avg



gNArgs, gNumbers, gSum, gAvg = sum_nums(10, 20, 30)

print(f'{gNArgs}개의 인자 {gNumbers}')
print(f'합계 : {gSum}, 평균 : {gAvg}')

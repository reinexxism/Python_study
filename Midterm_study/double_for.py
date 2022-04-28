for i in range(2, 10):  #외부 for loop
  for j in range(1, 10):  #내부 for loop
    print('{} * {} = {:2d}'.format(i, j, i*j), end='')
  print()   #내부 loop 수행 후 줄바꿈을 함
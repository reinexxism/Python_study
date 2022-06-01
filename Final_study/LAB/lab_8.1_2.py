# 1-1 코드의 Error
try : 
  a = [10, 20, 30]
  print(a[3])
except Exception as e :
  print('error of q.1 = ', e)

# 1-2 코드의 Error
try : 
  n = int('20%')
  print(n)
except Exception as e :
  print('error of q.2 = ', e)

# 1-3 코드의 Error
try : 
  a = 100 + '200'
  print(a)
except Exception as e :
  print('error of q.3 =', e)
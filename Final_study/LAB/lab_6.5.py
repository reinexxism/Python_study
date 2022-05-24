fruits_dic = {'apple' : 6000, 'melon' : 3000, 'banana' : 5000, 'orange' : 4000}

# dictionary의 모든 key를 list 형식으로 출력
print(list(fruits_dic.keys()))

# dictionary의 모든 value를 list 형식으로 출력
print(list(fruits_dic.values()))

# dictionary의 모든 항목의 개수를 len() fuctino을 통해 출력
print('fruits_dic 딕셔너리의 항목의 개수 : ', len(fruits_dic))


# dictionary에 'apple'과 'mango' 키가 있는가 검사하여 출력
# 'apple' key
if ('apple' in fruits_dic) : 
  print('apple is in fruits_dic')
else :
  print('apple is not in fruits_dic')

# 'mango' key
if ('mango' in fruits_dic) :
  print('mango is in fruits_dic')
else :
  print('mango is not in fruits_dic')
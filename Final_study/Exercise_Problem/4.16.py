n = list(map(int, input('쉼표로 구분된 정수를 여러 개 입력하세요 : ').split(',')))
#mlist = sorted(n)

mlist = []
for i in n :
  mlist.append(i)

mlist.sort()


print('입력된 정수의 리스트 : ', n)
print('정렬 된 정수의 리스트 : ', mlist)
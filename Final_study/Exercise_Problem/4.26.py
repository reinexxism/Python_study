input_city = ' Park(Java city), Kim(C city), Kang(Bython city), Lee(Bython city), Hong(Ruby city), Cho(Bython city), Koo(C city), Ryu(C++ city'

print('주어진 문자열 : ')
print(input_city)
print('수정된 문자열 : ')
print(input_city.replace('Bython', 'Python'))
print('Bython 문자열은 모두 {}번 수정했습니다.'.format(input_city.count('Bython')))
# 파일 추가(append) 모드를 이용한 파일 열기와 추가하기
f = open('foo.txt', 'a+')
f.write('This will be appended.\n')
f.write('This too.\n')
f.close()
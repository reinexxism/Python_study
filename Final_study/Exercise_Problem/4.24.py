sentence = input('여러 단어로 이루어진 글을 입력하세요 : ')
sentence = sentence.replace(':', ' ')
sentence = sentence.replace(',', ' ')
sentence = sentence.replace('.', ' ')
sentence = sentence.split()
sentence.sort()

print('정렬 결과 : ')
print(sentence)
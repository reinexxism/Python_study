# in 연산자를 이용한 딕셔너리 항목의 조회
person = { '이름' : '홍길동', '나이' : 26, '몸무게' : 82 }

print(len(person)) # 딕셔너리 항목의 개수를 반환
print('이름' in person) # '이름'은 키에 있음
print('직업' in person) # '직업'은 키에 없음
print('홍길동' in person) # '홍길동'은 값에 있으나 키에 없음 (주의)
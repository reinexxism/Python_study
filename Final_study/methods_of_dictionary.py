person = { '이름' : '홍길동', '나이' : 26, '몸무게' : 82}

# .keys() method : dictionary의 key들을 list형태로 반환
print(person.keys())

# .values() method : dictionary의 value들을 list형태로 반환
print(person.values())

# .items() method : dictionary의 [key]:[value]들을 list형태로 반환
print(person.items())

# .popitem() method : dictionary의 마지막 [key]:[value]를 선택하여 반환한 후 삭제
print(person.popitem())

# .pop() method : 특정 key의 value를 반환한 후 삭제
print(person.pop('나이'))

# .clear() method : dictionary의 모든 [key]:[value]가 삭제되어 빈 dictionary로 변환
print(person.clear())
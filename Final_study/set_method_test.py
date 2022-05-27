s = {100, 100, 200, 200, 300, 400} # 중복원소 100, 200이 존재함

print(s) # 중복되는 원소인 100과 200인 하나만 출력

# s 집합에 원소 500을 새로 추가 : add() method
s.add(500) 
print(s)

# s 집합에 원소 100을 삭제 : discard() method
s.discard(100)
print(s)
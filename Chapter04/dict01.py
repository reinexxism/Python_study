# 딕셔너리를 선언
dictionary = {
  "name": "7D 건조 망고",
  "type": "당절임",
  "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
  "origin": "필리핀"
}

# Output
print("name :", dictionary["name"])
print("type :", dictionary["type"])
print("ingredient :", dictionary["ingredient"])
print("origin :", dictionary["origin"])
print()

# Change value of dictionary
dictionary["name"] = "8D 건조 망고"
print("name :", dictionary["name"])
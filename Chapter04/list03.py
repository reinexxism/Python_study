list_a = [0, 1, 2, 3, 4, 5]
print("# 리스트의 요소 하나 제거하기")

# Solution1 - del keyword
del list_a[1] 
print("del list_a[1] =", list_a) # del 리스트명[Index]

# Solution2 - pop() function
list_a.pop(2)
print("list_a.pop(2) =", list_a) # 리스트명.pop(Index)
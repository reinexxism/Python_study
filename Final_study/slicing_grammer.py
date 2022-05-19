a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. a_list[start:end] = start부터 (end-1)까지의 항목들을 슬라이싱 (end인덱스의 항목은 포함하지 않음)

# 2. a_list[start:] = start부터 list의 끝까지, 즉 뒷부분 모두를 슬라이싱

# 3. a_list[:end] = 처음부터 (end-1)번째 인덱스 항목까지를 슬라이싱

# 4. a_list[:] = list 전체를 슬라이싱

# 5. a_list[start:end:step] = start부터 (end-1)까지를 step만큼 건너뛰며 슬라이싱

# 6. a_list[-2:] = 뒤에서부터 두 개의 항목을 슬라이싱

# 7. a_list[:-2] = 처음부터 끝의 두 개를 제외한 모든 항목을 슬라이싱

# 8. a_list[::-1] = 모든 항목을 역순으로 가져옴

# 9. a_list[1::-1] = 처음 두 개 항목을 역순으로 슬라이싱
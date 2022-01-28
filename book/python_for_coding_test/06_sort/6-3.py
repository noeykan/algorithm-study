# 삽입정렬
# 처음 푼 것
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(1, len(array)):
    for j in range(i):
        if array[i] < array[j]:
            array = array[:j] + [array[i]] + array[j:i] + array[i+1:]
            break
print(array)

# 중간에 데이터를 껴 넣는 생각만 해서 array를 슬라이싱 해서 겨우 만들었지만,
# 답지처럼 하는게 더 깔끔한 듯

# 답지 버전
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break
print(array)
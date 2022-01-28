# 선택정렬
# 처음 푼 것
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
N = len(array)
for i in range(0, N-1):
    min_value = array[i]
    min_idx = i
    for j in range(i+1, N):
        if array[j] < min_value:
            min_value = array[j]
            min_idx = j
    array[i], array[min_idx] = array[min_idx], array[i]

print(array)

# 1) 불필요한 변수들이 있음. min_idx만 있으면 되므로 min_value는 필요 없음
# 2) for문에서 귀찮게 N-1 안해도 N으로 해도 알고리즘 상 문제 없음

# 답지 풀이
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(len(array)):
    min_idx = i
    for j in range(i + 1, len(array)):
        if array[j] < array[i]:
            min_idx = j
    array[i], array[min_idx] = array[min_idx], array[i]

print(array)

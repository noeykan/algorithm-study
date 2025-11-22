# 251121

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
# 5 7 [9] 0 3
# 5 7 9 [0] 3
# 0 5 7 9 [3]
# 0 3 5 7 9

# 처음 푼 풀이
# for i in range(1, len(array)):
#     target = i
#     for j in range(i):
#         if array[i] < array[j]:
#             target = j
#             break
#     for k in range(i, target, -1):
#         array[k], array[k - 1] = array[k - 1], array[k]
# print(array)

# 처음 이렇게 풀었는데, 굳이 for문 한번 더 돌려서 target을 정하고 거기까지 할 필요가 없음
# 그냥 바로바로 swap 하면서 판단해서 멈추면 됨.

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j - 1] < array[j]:
            break
        array[j - 1], array[j] = array[j], array[j - 1]
print(array)
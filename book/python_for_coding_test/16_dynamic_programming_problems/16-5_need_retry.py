# 35. 못생긴 수

N = int(input())

# 내풀이: O(n^2)
d = [float('inf')] * N
d[0] = 1

mul = [2, 3, 5]
for i in range(1, N):
    for j in range(i - 1, -1, -1):
        for m in mul:
            candidate = d[j] * m
            if d[i - 1] < candidate:
                d[i] = min(d[i], candidate)
print(d[-1])

# 풀긴 풀었으나 시간 복잡도가 O(n^2) 라서 내 알고리즘은 별로임
# 아래 답지 알고리즘을 이해하고 나중에 다시 풀어보자.. 이런 생각을 어떻게 하지

# # 답지풀이: O(n)
# d = [0] * N
# d[0] = 1

# i2 = i3 = i5 = 0
# next2 = 2
# next3 = 3
# next5 = 5

# for i in range(1, N):
#     d[i] = min(next2, next3, next5)
#     if d[i] == next2:
#         i2 += 1
#         next2 = d[i2] * 2
#     if d[i] == next3:
#         i3 += 1
#         next3 = d[i3] * 3
#     if d[i] == next5:
#         i5 += 1
#         next5 = d[i5] * 5
# print(d)


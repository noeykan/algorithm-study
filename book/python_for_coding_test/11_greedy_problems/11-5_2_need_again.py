# 251203

n, m = map(int, input().split())
data = list(map(int, input().split()))

# 1. 내가 푼 문제
# data.sort()

# cnt = n * (n - 1) / 2 # nC2
# cnt_same = 1
# prev_data = -1
# for d in data:
#     if d == prev_data:
#         cnt_same += 1
#     else:
#         if cnt_same > 1:
#             cnt -= (cnt_same * (cnt_same - 1) / 2)
#         prev_data = d
#         cnt_same = 1
# if cnt_same > 1:
#     cnt -= (cnt_same * (cnt_same - 1) / 2)

# print(int(cnt))

# 12m
# 수학으로 풀었음...

# 2. 답지 설명 보고 다시 푼 문제
balls = [0] * (m + 1)
cnt = 0
for d in data:
    balls[d] += 1

for i in range(1, m + 1):
    if balls[i] > 0:
        n -= balls[i]
        cnt += balls[i] * n

print(cnt)


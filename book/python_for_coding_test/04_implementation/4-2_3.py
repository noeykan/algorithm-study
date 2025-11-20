# 251120
n = int(input())

# 초
# 03 13 23 43 53 : 5개
# 3X : 10개
# 0~59 : 10 + 5 = 15개
# 60개중 3이 포함되어있는 경우는 15개, 아닌건 45개

# 분
# 분에 3이 포함 : 15 * 60
# 분에 3이 안포함 : 45 * 15

# i = 0
# cnt = 0
# while i <= n:
#     if i < 10:
#         if i == 3:
#             cnt += (60 * 60)
#         else:
#             cnt += (15 * 60) + (45 * 15)
#     else:
#         if i // 10 == 3 or i % 10 == 3:
#             cnt += (60 * 60)
#         else:
#             cnt += (15 * 60) + (45 * 15)
#     i += 1
# print(cnt)

# 16m
# t:O(n) s:O(1)
# 수학적으로 풀어서, 최적화 시킨 코드는 맞지만 결과론적으로 시간이 15m 초과하였고 조금만 실수하면 틀릴 수 있으므로 그냥 세자...

# 그냥 세는 코드
cnt = 0
for h in range(n + 1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) or '3' in str(m) or '3' in str(s):
                cnt += 1
print(cnt)

# if '3' in str(h) + str(m) + str(s): 이게 더 효율적!
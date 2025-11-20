# 251120

n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data_desc = sorted(data, reverse=True)
first = data_desc[0]
second = data_desc[1]

# 1
# i = m
# max_cnt = k
# ans = 0
# while i > 0:
#     if max_cnt > 0:
#         ans += first
#         max_cnt = max_cnt - 1
#     else:
#         ans += second
#         max_cnt = k 
#     i = i - 1
# print(ans)

# 2
q, r = divmod(m, (k + 1))
ans = q * (first * k + second) + r * first
print(ans)
# 251120

n, k = map(int, input().split())

# 1. 내가 푼 거
# cnt = 0
# while n != 1:
#     if (n % k) == 0:
#         n = n // k
#     else:
#         n -= 1
#     cnt += 1
# print(cnt)

# 4.5m
# n이 100억 이상의 큰 수에서는 비효율적!

# 2. 책 힌트 보고 다시 푼 것
cnt = 0
while n != 1:
    q, r = divmod(n, k)
    if q > 0:
        cnt += (r + 1)
        n = q
    else:
        cnt += (r - 1)
        break
print(cnt)

# 주의: divmod 할때 나누는 수가 더 클때를 고려해야 함!
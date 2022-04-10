# https://www.acmicpc.net/problem/2581
# 소수

import math

m = int(input())
n = int(input())
INF = int(1e9)
is_prime = [True] * 10001
is_prime[1] = False
total_sum = 0
min_value = INF

for i in range(2, int(math.sqrt(n)) + 1):
    if is_prime[i] == True:
        j = 2
        while i * j <= n:
            is_prime[i * j] = False
            j += 1

for i in range(m, n + 1):
    if is_prime[i] == True:
        total_sum += i
        if min_value == INF:
            min_value = i

if total_sum == 0:
    print(-1)
else:
    print(total_sum)
    print(min_value)

# 처음에 틀려서 의아했는데 생각해보니 input이 1도 들어올 수 있기에 소수가 아님을 처리 해주고 나니 맞았음
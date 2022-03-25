# A. 유사 라임 게임

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, L, F = map(int, input().split())
    data = input().split()
    for i in range(n):
        data[i] = data[i][::-1]
    data.sort()
    cnt = 0
    counted = [False] * n
    for i in range(n - 1):
        if counted[i]:
            continue
        if data[i][:F] == data[i + 1][:F]:
            cnt += 1
            counted[i] = counted[i + 1] = True
    print(cnt)
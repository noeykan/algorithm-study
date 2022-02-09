# 5. 효율적인 화폐 구성

N, M = map(int, input().split())
pay = [int(input()) for _ in range(N)]

d = [0] * 10001
for p in pay:
    d[p] = 1

def get_min_cnt(n):
    if d[n] == 0:
        min_cnt = 10001
        for p in pay:
            if n - p > 0:
                prev_cnt = get_min_cnt(n - p)
                if prev_cnt == 0:
                    min_cnt = 0
                else:
                    min_cnt = min(min_cnt, preve_cnt + 1)
        d[n] = min_cnt if min_cnt != 10001 else 0
    return d[n]

answer = get_min_cnt(M)
if answer != 0:
    print(answer)
else:
    print(-1)

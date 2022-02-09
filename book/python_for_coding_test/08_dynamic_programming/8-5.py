# 2. 1로 만들기

x = int(input())

# d(1) = 0
# d(2) = 1
# d(3) = 1
# d(4) = d(2) + 1
# d(5) = 1

# 1. 탑다운(메모이제이션)
d = [-1] * 30001
d[1] = 0
def calc(n):
    if d[n] != -1:
        return d[n]

    min_cnt = calc(n - 1)
    if (n % 5) == 0:
        min_cnt = min(min_cnt, calc(n // 5))
    if (n % 3) == 0:
        min_cnt = min(min_cnt, calc(n // 3))
    if (n % 2) == 0:
        min_cnt = min(min_cnt, calc(n // 2))

    d[n] = min_cnt + 1
    return d[n]

print(calc(x))

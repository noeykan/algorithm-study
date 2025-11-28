#251123

n, m = map(int, input().split())
types = [int(input()) for _ in range(n)]

d = [float('inf')] * 10001
for t in types:
    d[t] = 1

for i in range(1, m + 1):
    for t in types:
        if i - t > 0 and d[i - t] <= 10000:
            d[i] = min(d[i], d[i - t] + 1)

if d[m] > 10000:
    print('-1')
else:
    print(d[m])

# 답지랑 살짝 다른데 로직은 똑같음. 답지 풀이가 좀 더 세련되었음
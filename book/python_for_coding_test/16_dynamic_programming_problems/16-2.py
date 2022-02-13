# 32. 정수 삼각형

N = int(input())
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))

d = [[0] * n for n in range(1, N + 1)]
d[0][0] = data[0][0]
for i in range(1, N):
    for j in range(i + 1):
        max_sum = 0
        if j == 0:
            max_sum = d[i - 1][j]
        elif j == i:
            max_sum = d[i - 1][j - 1]
        else:
            max_sum = max(d[i - 1][j - 1], d[i - 1][j])
        d[i][j] = max_sum + data[i][j]
print(max(d[N - 1]))

# 제한시간(30분) 이내에 풀음
# https://www.acmicpc.net/problem/1932
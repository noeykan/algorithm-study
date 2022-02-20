# 38. 정확한 순위

import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

answer = 0
connected = [0] * (n + 1)
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] != INF:
            connected[i] += 1
            connected[j] += 1

for c in connected:
    if c == n - 1:
        answer += 1

print(answer)

# 시간제한(40분) 내에 풀었음
# 마지막에 체크하는 부분에서 답지의 방식이 더 세련되었기 때문에 알아두면 좋을듯
# 각 i 학생에 대해서 graph[i][j] != INF or graph[j][i] != INF 일 때 count 를 증가시킨다
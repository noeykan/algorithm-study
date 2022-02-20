# 2. 미래 도시

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
    src, dest = map(int, input().split())
    graph[src][dest] = 1
    graph[dest][src] = 1
x, k = map(int, input().split())

# 1 -> k -> x
for p in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][p] + graph[p][j])

answer = graph[1][k] + graph[k][x]
if answer >= INF:
    print(-1)
else:
    print(answer)
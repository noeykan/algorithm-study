#251123

# #INPUT1
# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5

# #INPUT2
# 4 2
# 1 3
# 2 4
# 3 4

import sys
import heapq
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for p in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][p] + graph[p][j])

answer = graph[1][k] + graph[k][x]
if answer >= INF:
    print("-1")
else:
    print(answer)

# 35m
# 처음에 다익스트라인줄알고 다구현해놨다가 처음부터 다시함..
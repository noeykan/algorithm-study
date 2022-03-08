# 위상정렬
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
entries = [0] * (n + 1)
visited = [False] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    entries[b] += 1
answer = []
q = deque([])

for node in range(1, n + 1):
    if visited[node] is False and entries[node] == 0:
        q.append(node)

while q:
    
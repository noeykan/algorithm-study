# 40. 숨바꼭질

import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))
distance = [INF] * (n + 1)

def dijkstra(start):
    q = []
    distance[1] = 0
    heapq.heappush(q, (0, 1))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for des, d in graph[now]:
            tot_dist = dist + d
            if tot_dist < distance[des]:
                distance[des] = tot_dist
                heapq.heappush(q, (tot_dist, des))

dijkstra(1)

max_dist = max(distance[1:])
idx = distance.index(max_dist)
cnt = distance[1:].count(max_dist)
print(idx, max_dist, cnt)

# sample input
# 6 7
# 3 6
# 4 3
# 3 2
# 1 3
# 1 2
# 2 4
# 5 2

# 제한시간(40분) 내에 풀음
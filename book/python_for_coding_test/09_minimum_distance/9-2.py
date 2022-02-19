# 개선된 다익스트라 알고리즘 소스

# sample input
# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(m + 1)]
for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
distance = [INF] * (n + 1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for end, cost in graph[node]:
            tot_cost = dist + cost
            if tot_cost < distance[end]:
                distance[end] = tot_cost
                heapq.heappush(q, (tot_cost, end))

dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])

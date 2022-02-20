# 전보
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, dist = map(int, input().split())
    graph[a].append((b, dist))

distance = [INF] * (n + 1)

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for des, d in graph[node]:
            tot_dist = dist + d
            if tot_dist < distance[des]:
                distance[des] = tot_dist
                heapq.heappush(q, (tot_dist, des))

dijkstra(c)
max_dist = 0
cities = 0
for i in range(1, n + 1):
    if i != c and distance[i] < INF:
        cities += 1
        max_dist = max(max_dist, distance[i])

print(cities, max_dist)
#251123

import heapq
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
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for dest, dest_dist in graph[now]:
            cost = dist + dest_dist
            if cost < distance[dest]:
                distance[dest] = cost
                heapq.heappush(q, (cost, dest))

dijkstra(c)

cnt = 0
max_dist = 0
for i in range(1, n + 1):
    if i != c and distance[i] < INF:
        cnt += 1
        max_dist = max(max_dist, distance[i])

print(cnt, max_dist)
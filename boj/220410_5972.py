# https://www.acmicpc.net/problem/5972
# 택배 배송

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, dist = map(int, input().split())
    graph[a].append((b, dist))
    graph[b].append((a, dist))

def dijkstra():
    q = []
    distance[1] = 0
    heapq.heappush(q, (0, 1))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for n_dest, n_dist in graph[now]:
            cost = dist + n_dist
            if cost < distance[n_dest]:
                distance[n_dest] = cost
                heapq.heappush(q, (cost, n_dest))

dijkstra()
print(distance[n])

# 삽질포인트 2
# 1. 단방향 그래프로 구현했는데 문제는 양방향이었음
# 2. graph에 넣을때랑 q에 넣을때랑 cost 순서가 다른데, graph에서 뺄 때도 q처럼 cost를 먼저 빼는 걸로 처리해버렸음
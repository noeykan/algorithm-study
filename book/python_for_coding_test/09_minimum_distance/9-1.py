# 간단한 다익스트라 알고리즘 소스

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
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(m + 1)]
for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
distance = [INF] * (n + 1)
visited = [False] * (n + 1)

def get_smallest_node():
    dist = INF
    node = 0
    for i in range(1, n + 1):
        if visited[i] is False and distance[i] < dist:
            node = i
            dist = distance[i]
    return node

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for end, cost in graph[start]:
        distance[end] = cost
    for _ in range(1, n + 1):
        now = get_smallest_node()
        visited[now] = True
        for end, cost in graph[now]:
            total_cost = distance[now] + cost
            if total_cost < distance[end]:
                distance[end] = total_cost

dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])

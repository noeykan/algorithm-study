# 39. 화성탐사

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
di = [1, 0, -1, 0]
dj = [0, -1, 0, 1]

tc = int(input())
for _ in range(tc):
    n = int(input())
    distance = [[INF] * n for _ in range(n)]
    graph = [list(map(int, input().split())) for _ in range(n)]
    distance[0][0] = graph[0][0]
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))
    while q:
        dist, i, j = heapq.heappop(q)
        if distance[i][j] < dist:
            continue
        for x in range(4):
            ni = i + di[x]
            nj = j + dj[x]
            if 0 <= ni < n and 0 <= nj < n:
                tot_dist = dist + graph[ni][nj]
                if tot_dist < distance[ni][nj]:
                    distance[ni][nj] = tot_dist
                    heapq.heappush(q, (tot_dist, ni, nj))
    print(distance[n - 1][n - 1])

# sample input
# 3
# 3
# 5 5 4
# 3 9 1
# 3 2 7
# 5
# 3 7 2 0 1
# 2 8 0 9 1
# 1 2 1 8 1
# 9 8 9 2 0
# 3 6 5 1 5
# 7
# 9 0 5 1 1 5 3
# 4 1 2 1 6 5 3
# 0 7 6 1 6 8 5
# 1 1 7 8 3 2 3
# 9 4 0 7 6 4 1
# 5 8 3 2 4 8 3
# 7 4 8 4 8 3 4

# 제한시간(40분) 내에 풀음
# 과연 이 문제가 어떤 유형인지 모르는 상태에서 이 문제를 내가 다익스트라로 풀 수 있을까..? 잘 눈여겨보자
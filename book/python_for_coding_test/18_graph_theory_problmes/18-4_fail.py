# 44. 행성 터널

import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())

def get_cost(x, y):
    return min(abs(x[0]-y[0]), abs(x[1]-y[1]), abs(x[2]-y[2]))

stars = [list(map(int, input().split())) + [i] for i in range(n)]

# 1. 첫번째 시도 실패 - 메모리 초과
# graph = [(get_cost(stars[i], stars[j]), i, j) for i in range(n - 1) for j in range(i + 1, n)]

# 2. 두번째 시도 실패 - 시간 초과
# graph 모두 다 넣지 않고 제일 작은 cost만 골라서 넣은 버전
# graph = []
# for i in range(n):
#     min_cost = INF
#     for j in range(n):
#         if i != j:
#             min_cost = min(min_cost, get_cost(stars[i], stars[j]))
#     graph.append((min_cost, i, j))

# 3. 세번째 시도 - 답지 해설 보고 완료
graph = []
for i in range(3):
    s = sorted(stars, key=lambda x: x[i])
    for j in range(n - 1):
        graph.append((get_cost(s[j], s[j + 1]), s[j][3], s[j + 1][3]))

graph.sort()
parent = [x for x in range(n)]

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, x, y):
    xp = find_parent(parent, x)
    yp = find_parent(parent, y)
    if xp < yp:
        parent[yp] = xp
    else:
        parent[xp] = yp

total_cost = 0
for cost, a, b in graph:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        total_cost += cost

print(total_cost)

# # https://www.acmicpc.net/problem/2887
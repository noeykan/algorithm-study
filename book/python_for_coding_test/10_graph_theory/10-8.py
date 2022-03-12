# 3. 도시 분할 계획

# sample input
# 7 12
# 1 2 3
# 1 3 2
# 3 2 1
# 2 5 2
# 3 4 4
# 7 3 6
# 5 1 5
# 1 6 2
# 6 4 1
# 6 5 3
# 4 5 3
# 6 7 4

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
edges = []
parent = [x for x in range(n + 1)]
for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort()

def find_parent(p, x):
    if p[x] != x:
        p[x] = find_parent(p, p[x])
    return p[x]

def union_parent(p, x, y):
    xp = find_parent(p, x)
    yp = find_parent(p, y)
    if xp < yp:
        p[yp] = xp
    else:
        p[xp] = yp

total_cost = 0
latest_cost = 0
for cost, a, b in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        total_cost += cost
        latest_cost = cost

# 이 부분을 내가 넣고 하였으나 결과적으로 이 if문이 없어야 제대로 정답이 나옴
# if parent[1:].count(1) == n:
total_cost -= latest_cost
print(total_cost)

# 위와 같이 풀었으나 백준에서 30% 정도 되었을때 틀렸다고 나옴...
# 답지를 보니 위 if 문 한줄을 없이 풀었음...! 내가 오바해서 생각했나봄
# https://www.acmicpc.net/problem/1647

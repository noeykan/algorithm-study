# 43. 어두운 길

# sample input
# 7 11
# 0 1 7
# 0 3 5
# 1 2 8
# 1 3 9
# 1 4 7
# 2 4 5
# 3 4 15
# 3 5 6
# 4 5 8
# 4 6 9
# 5 6 11

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [x for x in range(n)]
edges = []
for _ in range(m):
    x, y, cost = map(int, input().split())
    edges.append((cost, x, y))
edges.sort()

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

total_save = 0
for cost, x, y in edges:
    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
    else:
        total_save += cost
print(total_save)




# 크루스칼 알고리즘

# input example
# 7 9
# 1 2 29
# 1 5 75
# 2 3 35
# 2 6 34
# 3 4 7
# 4 6 23
# 4 7 13
# 5 6 53
# 6 7 25

import sys

input = sys.stdin.readline
n, m = map(int, input().split())
items = []
for _ in range(m):
    a, b, dist = map(int, input().split())
    items.append((dist, (a, b)))
items.sort()
parent = [x for x in range(0, n + 1)] # index starts with 1

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, x, y):
    x_p = find_parent(parent, x)
    y_p = find_parent(parent, y)
    if x_p < y_p:
        parent[y_p] = x_p
    else:
        parent[x_p] = y_p

total_cost = 0
for i in range(m):
    cost, (a, b) = items[i]
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        total_cost += cost

print(total_cost)

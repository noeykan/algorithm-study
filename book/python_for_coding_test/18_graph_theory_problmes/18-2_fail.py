# 42. 탑승구

import sys
input = sys.stdin.readline

g = int(input())
p = int(input())

cnt = 0
parent = [x for x in range(g + 1)]

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

for _ in range(p):
    x = int(input())
    if find_parent(parent, x) != 0:
        union_parent(parent, x, x-1)
        cnt += 1

print(cnt)

# # 답지 보고 품... 대박... 이걸 어떻게 생각해내냐.. 그래프 문제인거 알면서도 엄청 오래 생각했는데 생각을 못 해냈음...

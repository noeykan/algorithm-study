# 2. 팀 결성

# sample input
# 7 8
# 0 1 3
# 1 1 7
# 0 7 6
# 1 7 1
# 0 3 7
# 0 4 2
# 0 1 1
# 1 1 1

n, m = map(int, input().split())
parent = [x for x in range(0, n + 1)]

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(x, y):
    xp = find_parent(x)
    yp = find_parent(y)
    if xp < yp:
        parent[y] = xp
    elif xp > yp:
        parent[x] = yp

for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        # 합치기
        union_parent(a, b)
    elif op == 1:
        # 같은팀확인
        if find_parent(a) == find_parent(b):
            print("YES")
        else:
            print("NO")
    else:
        print("Invalid input")

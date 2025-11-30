# 251129

# INPUT
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

parent = [i for i in range(n + 1)]

def get_parent(a):
    if parent[a] != a:
        parent[a] = get_parent(parent[a])
    return parent[a]    

def union_parent(a, b):
    ap = get_parent(a)
    bp = get_parent(b)
    if ap < bp:
        parent[bp] = ap
    else:
        parent[ap] = bp

for _ in range(m):
    op, a, b = map(int, input().split())
    if op:
        if get_parent(a) == get_parent(b):
            print('YES')
        else:
            print('NO')
    else:
        union_parent(a, b)
# 251129

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

n, m = map(int, input().split())

parent = [i for i in range(n + 1)]
data = []

for _ in range(m):
    a, b, c = map(int, input().split())
    data.append((c, a, b))

data.sort()

def get_parent(a):
    if parent[a] != a:
        parent[a] = get_parent(parent[a])
    return parent[a]

def make_union(a, b):
    ap = get_parent(a)
    bp = get_parent(b)
    if ap < bp:
        parent[bp] = ap
    else:
        parent[ap] = bp

total_dist = 0
max_dist = 0
for dist, a, b in data:
    if get_parent(a) != get_parent(b):
        make_union(a, b)
        total_dist += dist
        max_dist = max(max_dist, dist)

print(total_dist - max_dist)


# 251129

# Sample Input
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

v, e = map(int, input().split())

data = [tuple(map(int, input().split())) for _ in range(e)]
data.sort(key=lambda x: x[2])

parent = [i for i in range(v + 1)]

total_dist = 0

def get_parent(a):
    if parent[a] != a:
        parent[a] = get_parent(parent[a])
    return parent[a]

def union_parent(a, b):
    a_parent = get_parent(a)
    b_parent = get_parent(b)
    if a_parent < b_parent:
        parent[b_parent] = a_parent
    else:
        parent[a_parent] = b_parent

for a, b, dist in data:
    if get_parent(a) != get_parent(b):
        union_parent(a, b)
        total_dist += dist

print(total_dist)
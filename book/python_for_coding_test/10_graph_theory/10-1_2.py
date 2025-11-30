#251128

v, e = map(int, input().split())

parent = [i for i in range(v + 1)]

def get_parent(a):
    while parent[a] != a:
        a = parent[a]
    return a

def union_function(a, b):
    a_parent = get_parent(a)
    b_parent = get_parent(b)
    if a_parent < b_parent:
        parent[b_parent] = a_parent
    else:
        parent[a_parent] = b_parent

for _ in range(e):
    a, b = map(int, input().split())
    union_function(a, b)

print("각 원소가 속한 집합:", end=' ')
for i in range(1, v + 1):
    print(get_parent(i), end=' ')

print("\n부모 테이블:", end=' ')
for i in range(1, v + 1):
    print(parent[i], end=' ')
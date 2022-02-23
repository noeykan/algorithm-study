# 서로소 집합 알고리즘
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [x for x in range(0, n + 1)]

def find_parent(parent, x):
    if parent[x] != x:
        find_parent(parent, parent[x])
    return x

def union_parent(parent, a, b):
    a_p = find_parent(parent, a)
    b_p = find_parent(parent, b)
    if a_p < b_p:
        parent[b_p] = a_p
    else:
        parent[a_p] = b_p

for _ in range(m):
    a, b = map(int, input().split())
    union_parent(parent, a, b)
    print(parent)

print('각 원소가 속한 집합: ', end='')
for i in range(1, n + 1):
    print(find_parent(parent, i), end=' ')
print()

print('부모 테이블: ', end='')
for i in range(1, n + 1):
    print(parent[i], end=' ')
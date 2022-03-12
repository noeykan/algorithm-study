# 41. 여행계획

# sample input
# 5 4
# 0 1 0 1 1
# 1 0 1 1 0
# 0 1 0 0 0
# 1 1 0 0 0
# 1 0 0 0 0
# 2 3 4 3

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
plan = list(map(int, input().split()))

def find_parent(p, x):
    if p[x] != x:
        p[x] = find_parent(p, p[x])
    return p[x]

def union_parent(p, x, y):
    px = find_parent(p, x)
    py = find_parent(p, y)
    if px < py:
        p[y] = px
    else:
        p[x] = py

parent = [x for x in range(n + 1)]
for a in range(n):
    for b in range(n):
        if graph[a][b] == 1:
            union_parent(parent, a + 1, b + 1)

prev = find_parent(parent, plan[0])
answer = True
for p in plan[1:]:
    now = find_parent(parent, p)
    if now == prev:
        prev = now
    else:
        answer = False
        break

if answer:
    print("YES")
else:
    print("NO")

# 제한시간(40분) 내에 문제 풀음
# prev를 정하고 now와 비교하는 것 보다 처음부터 i, i+1 로 비교하면서 for문 타는게 더 깔끔할듯
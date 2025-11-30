# 251129

# INPUT
# 7 8
# 1 2
# 1 5
# 2 3
# 2 6
# 3 4
# 4 7
# 5 6
# 6 4

from collections import deque

v, e = map(int, input().split())
edges = {}
for i in range(1, v + 1):
    edges[i] = []

in_degrees = [0] * (v + 1)
visited = [0] * (v + 1)

for _ in range(e):
    a, b = map(int, input().split())
    edges[a].append(b)
    in_degrees[b] += 1

q = deque([])

for i in range(1, v + 1):
    if in_degrees[i] == 0 and visited[i] == 0:
        q.append(i)
        visited[i] = 1

while q:
    node = q.popleft()
    print(node, end=' ')
    for c in edges[node]:
        in_degrees[c] -= 1

    # FIXME: for문으로 노드 개수만큼 계속 반복해서 도는 것으로 비효율적임
    # 아래 없애고 그냥 위 for문 안에서 처리하면 되잖아? 그러면 visited도 필요 없음!!
    for i in range(1, v + 1):
        if in_degrees[i] == 0 and visited[i] == 0:
            q.append(i)
            visited[i] = 1


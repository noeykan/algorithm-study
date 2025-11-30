#251129

# sample input
# 5
# 10 -1
# 10 1 -1
# 4 1 -1
# 4 3 1 -1
# 3 3 -1

from collections import deque

n = int(input())

hours = [0] * (n + 1)
in_degrees = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
graph_back = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    data = list(map(int, input().split()))
    hours[i] = data[0]
    for j in range(1, len(data) - 1):
        graph_back[i].append(data[j])
        graph[data[j]].append(i)
        in_degrees[i] += 1

q = deque([])
for i in range(1, n + 1):
    if in_degrees[i] == 0:
        q.append(i)

while q:
    node = q.popleft()
    max_hours = 0
    for prev in graph_back[node]:
        max_hours = max(max_hours, hours[prev])
    hours[node] += max_hours

    for next in graph[node]:
        in_degrees[next] -= 1
        if in_degrees[next] == 0:
            q.append(next)

for i in range(1, n + 1):
    print(hours[i])

# graph_back이랑 graph 둘다 썼는데, graph_back은 필요가 없었네?
# 굳이 현재 노드 기준으로 hours 업데이트 하려고 graph_back썼는데 그럴필요없이 graph 쓰고 다음노드 hours 업데이트하면됨
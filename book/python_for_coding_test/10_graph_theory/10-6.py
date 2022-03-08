# 위상정렬

# sample input
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

# 처음 내가 푼 코드
# n, m = map(int, input().split())
# graph = [[] for _ in range(n + 1)]
# entries = [0] * (n + 1)
# visited = [False] * (n + 1)
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     entries[b] += 1
# answer = []
# q = deque([])
#
# for node in range(1, n + 1):
#     if visited[node] is False and entries[node] == 0:
#         q.append(node)
#
# while q:
#     print(q)
#     a = q.popleft()
#     for b in graph[a]:
#         entries[b] -= 1
#     graph[a].clear()
#     answer.append(a)
#     visited[a] = True
#     for node in range(1, n + 1):
#         if visited[node] is False and entries[node] == 0 and node not in q:
#             q.append(node)
#
# for node in answer:
#     print(node, end=' ')

# 내 풀이는 원리는 같지만 군더더기 코드가 많다 답지 풀이를 보고 이해하고 숙지하자

# 답지보고 정리한 코드
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
entries = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    entries[b] += 1
answer = []
q = deque([])

for node in range(1, n + 1):
    if entries[node] == 0:
        q.append(node)

while q:
    a = q.popleft()
    answer.append(a)
    for b in graph[a]:
        entries[b] -= 1
        if entries[b] == 0:
            q.append(b)

for node in answer:
    print(node, end=' ')
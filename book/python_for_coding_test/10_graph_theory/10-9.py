# 4. 커리큘럼

# sample input
# 5
# 10 -1
# 10 1 -1
# 4 1 -1
# 4 3 1 -1
# 3 3 -1

# 처음 푼 코드
# from collections import deque
#
# n = int(input())
# time = [0] * (n + 1)
# graph = [[] for _ in range(n + 1)]
# total_time = [0] * (n + 1)
# indegree = [0] * (n + 1)
# candidate = [[0] for _ in range(n + 1)]
#
# for i in range(1, n + 1):
#     data = list(map(int, input().split()))
#     time[i] = data[0]
#     for d in data[1:-1]:
#         graph[d].append(i)
#         indegree[i] += 1
#
# q = deque([])
# for i in range(1, n + 1):
#     if indegree[i] == 0:
#         q.append(i)
#
# while q:
#     i = q.popleft()
#     total_time[i] = max(candidate[i]) + time[i]
#     for ni in graph[i]:
#         indegree[ni] -= 1
#         candidate[ni].append(total_time[i])
#         if indegree[ni] == 0:
#             q.append(ni)
#
# print(*total_time[1:], sep='\n')

# 제한시간(50분) 초과하였지만 풀었음!
# 이게 위상정렬 카테고리라는 걸 몰랐으면 절대 손도 못 댈 것 같았던 문제;;
# 답지 코드가 내 코드보다 쓰는 변수도 더 적고 깔끔하니 아래 참조..!
# 내 코드서 candidate 변수가 들어가게 된 계기가, 노드를 처리 할 때 연결된 다음 노드의 리스트에 현재 노드의 누적 time 값을
# candidate 변수의 다음 노드 칸에 append 시켜서, 다음 노드를 처리 할 때 그 값들 중 max를 찾으려고 했던 것인데, 그럴 필요 없이
# 매 노드를 처리할 때 연결된 다음 노드의 누적 time값도 매번 계산이 가능 했었다..!

# 답지 코드

from collections import deque
import copy

n = int(input())
time = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for i in range(1, n + 1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for d in data[1:-1]:
        graph[d].append(i)
        indegree[i] += 1

total_time = copy.deepcopy(time)
q = deque([])
for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

while q:
    i = q.popleft()
    for ni in graph[i]:
        total_time[ni] = max(total_time[ni], total_time[i] + time[ni])
        indegree[ni] -= 1
        if indegree[ni] == 0:
            q.append(ni)

print(*total_time[1:], sep='\n')
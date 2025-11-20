# 251121

# INPUT
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111
from collections import deque

N, M = map(int, input().split())
data = [list(map(int, input())) for _ in range(N)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# 처음 푼 풀이. 30m.
# def bfs(i, j):
#     data[i][j] = 0
#     cnt = 1

#     queue = deque()
#     queue.append((i, j, cnt))
    
#     while queue:
#         ci, cj, ccnt = queue.popleft()
#         if ci == N - 1 and cj == M - 1:
#             return ccnt
#         for k in range(4):
#             ni, nj = ci + di[k], cj + dj[k]
#             if 0 <= ni < N and 0 <= nj < M and data[ni][nj] == 1:
#                 data[ni][nj] = 0
#                 ncnt = ccnt + 1
#                 queue.append((ni, nj, ncnt))
# print(bfs(0, 0))

# 답지 보고 cnt를 queue에 넣지 않고 직접 data에 매핑하는 방식 다시 풀어봄
def bfs(i, j):
    cnt = 1
    data[i][j] = cnt

    queue = deque()
    queue.append((i, j))
    
    while queue:
        ci, cj = queue.popleft()
        if ci == N - 1 and cj == M - 1:
            return data[ci][cj]
        for k in range(4):
            ni, nj = ci + di[k], cj + dj[k]
            if 0 <= ni < N and 0 <= nj < M and data[ni][nj] == 1:
                data[ni][nj] = data[ci][cj] + 1
                queue.append((ni, nj))
print(bfs(0, 0))
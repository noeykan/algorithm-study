from itertools import combinations
from copy import deepcopy

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# 1. 내 방법
def dfs(board, i, j):
    for n in range(4):
        i_next = i + di[n]
        j_next = j + dj[n]
        if i_next < 0 or i_next >= N or j_next < 0 or j_next >= M:
            continue
        if board[i_next][j_next] == 0:
            board[i_next][j_next] = 2
            dfs(board, i_next, j_next)

virus = [(i, j) for i in range(N) for j in range(M) if board[i][j] == 2]
empty_rooms = [(i, j) for i in range(N) for j in range(M) if board[i][j] != 1 and board[i][j] != 2]
wall_picks = list(combinations(empty_rooms, 3))

max_safe_cnt = -1
for picks in wall_picks:
    b = deepcopy(board)
    # 벽 1로 만듦
    for p in picks:
        b[p[0]][p[1]] = 1

    for v in virus:
        dfs(b, v[0], v[1])

    safe_cnt = 0
    for i in range(N):
        for j in range(M):
            if b[i][j] == 0:
                safe_cnt += 1
    max_safe_cnt = max(max_safe_cnt, safe_cnt)

print(max_safe_cnt)

# 풀이시간 40분 딱 전에 다 풀고 정답 맞춤
# 1) 오잉? 근데 나는 combinations 랑 DFS 다 썼는데 답지는 DFS만 써서 해결했네?? 이게 가능했네???
#    답지 이해 안돼서 한참 보다가 겨우 이해했다... 이렇게 해도 컴비네이션이 구현 되는구나...!
#    나는 벽 구할때는 combinations 쓰고, 바이러스 전파할 때는 DFS 썼는데 여기서는 벽 구할때도 combinations 을 씀!
#    => 밑에 한번 이 방법대로 풀어보긴 함. BUT, 내가 쓴 방법이 연산량이 더 적음!! 답지의 DFS 두번이 더 헤비한 방법임
#    => 답지 방법은 백준 기준으로 ,python3 로는 시간초과 뜨고, pypy3 로만 통과하지만, 내 방법으로는 둘다 통과 :)
# 2) deepcopy 굳이 안쓰고 답지서는 board와 같은 이중배열 하나 더 선언해 두고, 여기에 계속 값 복사해서 씀..!
# https://www.acmicpc.net/problem/14502

# 답지 한번 보고 다시 구현 시도(combinations 없이)

# 2. 답지 방법

# result = 0
# board_virus = [[0] * M for _ in range(N)]
#
# def get_score():
#     score = 0
#     for i in range(N):
#         for j in range(M):
#             if board_virus[i][j] == 0:
#                 score += 1
#     return score
#
# def virus(i, j):
#     for n in range(4):
#         ni = i + di[n]
#         nj = j + dj[n]
#         if 0 <= ni < N and 0 <= nj < M:
#             if board_virus[ni][nj] == 0:
#                 board_virus[ni][nj] = 2
#                 virus(ni, nj)
#
# def dfs(count):
#     if count == 3:
#         for i in range(N):
#             for j in range(M):
#                 board_virus[i][j] = board[i][j]
#         for i in range(N):
#             for j in range(M):
#                 if board[i][j] == 2:
#                     virus(i, j)
#         global result
#         result = max(result, get_score())
#         return
#     for i in range(N):
#         for j in range(M):
#             if board[i][j] == 0:
#                 board[i][j] = 1
#                 dfs(count + 1)
#                 board[i][j] = 0
#
# dfs(0)
# print(result)
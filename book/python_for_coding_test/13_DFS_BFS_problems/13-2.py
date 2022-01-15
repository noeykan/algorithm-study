from itertools import combinations
from copy import deepcopy

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

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
# 오잉? 근데 나는 combinations 랑 DFS 다 썼는데 답지는 DFS만 써서 해결했네?? 이게 가능했네???

# https://www.acmicpc.net/problem/14502
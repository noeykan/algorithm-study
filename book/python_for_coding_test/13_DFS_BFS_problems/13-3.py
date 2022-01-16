N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

# 0부터 시작하는 걸로 인덱스 변환
I = X - 1
J = Y - 1

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

# 1. 시간 초과로 실패
# def spread(i, j, coord):
#     kind = board[i][j]
#     for n in range(4):
#         ni = i + di[n]
#         nj = j + dj[n]
#         if 0 <= ni < N and 0 <= nj < N:
#             if board[ni][nj] == 0:
#                 coord.add((ni, nj))
#
# def virus(kind):
#     coord = set([])
#     for i in range(N):
#         for j in range(N):
#             if board[i][j] == kind:
#                 spread(i, j, coord)
#     for c in coord:
#         board[c[0]][c[1]] = kind
#
# for sec in range(1, S+1):
#     for kind in range(1, K + 1):
#         virus(kind)
#
# print(board[I][J])


# 2. BFS
from collections import deque

# 디버깅용
def show():
    for i in range(N):
        print(*board[i], sep="")
    print("")

def bfs():
    q = deque([])
    for kind in range(1, K + 1):
        for i in range(N):
            for j in range(N):
                if board[i][j] == kind:
                    q.append((i, j, kind, 0))
    while q:
        i, j, kind, sec = q.popleft()
        if sec >= S:
            break
        for n in range(4):
            ni = i + di[n]
            nj = j + dj[n]
            if 0 <= ni < N and 0 <= nj < N:
                if board[ni][nj] == 0:
                    board[ni][nj] = kind
                    q.append((ni, nj, kind, sec + 1))
        # print(f"{sec+1}s")
        # show()

    return board[I][J]

print(bfs())

# 시간초과(50분) 하였음. 답이 계속 틀렸다고 나와서 답지 봄...
# 처음 풀이를 하였을때는 시간초과가 떴었고, 두번쨰로 BFS로 풀었을 때는 계속 답이 틀리다고 나옴...
# 이를 진짜 모르겠었는데 알고보니 삽질 했던 것... queue에다가 순서대로 넣을때 for kind 문이 맨 위에있었어야 했는데 맨 아래있었음...
# * 답지를 보니 이렇게 매번 N*N for문을 kind씩 반복하는게 아니라, q에 먼저 넣고 정렬 하는 방법을 썼던데 그게 더 효율적인듯.
# # https://www.acmicpc.net/problem/18405
N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]
# 보드에 0, 1, 2 등으로 쓸 것이라 중복되지 않게 1 부분을 -1로 바꿔줌
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            board[i][j] = -1

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

# DFS 방법
def dfs(board, i, j, cnt):
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
        return
    if board[i][j] != 0:
        return
    board[i][j] = cnt
    for n in range(len(di)):
        dfs(board, i + di[n], j + dj[n], cnt)

cnt = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            cnt += 1
            dfs(board, i, j, cnt)
print(cnt)

# BFS 방법 (DFS 로 풀고 답지 본 후 다시 BFS로 내가 푼 것)
# from collections import deque
#
# def bfs(x, y):
#     if board[x][y] != 0:
#         return False
#     queue = deque([[x, y]])
#     while queue:
#         x_now, y_now = queue.popleft()
#         board[x_now][y_now] = 1
#         for n in range(4):
#             i = x_now + di[n]
#             j = y_now + dj[n]
#             if i < 0 or i >= N or j < 0 or j >= M:
#                 continue
#             if board[i][j] == 0:
#                 queue.append([i, j])
#     return True
#
# cnt = 0
# for i in range(N):
#     for j in range(M):
#         if bfs(i, j) == True:
#             cnt += 1
# print(cnt)

# 시간초과(30분) 하여 1시간 걸림.. bfs로 해보려다가 잘 안되서 먼저 dfs로 풂
# 1) if board[i][j] == 0 이거 두번 하는 코드라서 맘에 안들어서 고민했었는데 답지를 보니,
#    이런 경우에 dfs에 return 값을 만들어서 True 일때만 cnt를 증가하는 식으로 하면 코드가 더 깔끔해진다!!
# 2) 나는 여기서 board[i][j]의 처음 1 값을 굳이 -1로 바꾸고 시작했는데, 그럴 필요가 없음.
#    board에 굳이 1, 2, 3 숫자를 새기려고 하지 않아도 main 함수에서 cnt만 증가시켜주면 됐음.
#    따라서 bfs 함수 파라미터도 4개가 아니라 i, j 두개만 있어도 될 뻔. board도 그냥 답지에서는 전역변수로 처리했더라.
#    len(board) 대신 N, M 도 그냥 함수에서 전역으로 쓰는 듯
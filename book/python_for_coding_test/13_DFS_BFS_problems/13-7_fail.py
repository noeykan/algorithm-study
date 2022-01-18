from collections import deque

N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


# 1. DFS/BFS 로 풀었는데 결국 시간/메모리 초과로 실패
#     뒤늦게 알았지만, DFS이건 BFS이건 tmp에 값을 넣는 것을 먼저 했어야 했음
#     그렇게 코드 수정 하니, 답이 제대로 맞음

# DFS 때 Recursion 에러 나서 추가함
# sys.setrecursionlimit(10**6)
# def dfs(tmp, i, j, nat):
#     global N, L, R
#     tmp[i][j] = nat
#     for n in range(4):
#         ni = i + di[n]
#         nj = j + dj[n]
#         if 0 <= ni < N and 0 <= nj < N:
#             diff = abs(board[i][j] - board[ni][nj])
#             if tmp[ni][nj] == -1 and L <= diff <= R:
#                 dfs(tmp, ni, nj, nat)

# def bfs(tmp, i, j, nat):
#     global N, L, R
#     q = deque([[i, j, nat]])
#     while q:
#         ii, jj, nnat = q.popleft()
#         tmp[ii][jj] = nnat
#         for n in range(4):
#             ni = ii + di[n]
#             nj = jj + dj[n]
#             if 0 <= ni < N and 0 <= nj < N:
#                 diff = abs(board[ii][jj] - board[ni][nj])
#                 if tmp[ni][nj] == -1 and L <= diff <= R:
#                     q.append([ni, nj, nat])

# loops = 0
# while True:
#     tmp = [[-1] * N for _ in range(N)]
#     nations = 0
#     for i in range(N):
#         for j in range(N):
#             if tmp[i][j] == -1:
#                 #dfs(tmp, i, j, nations)
#                 bfs(tmp, i, j, nations)
#                 nations += 1
    
#     cnt_sum = [[0, 0] for _ in range(nations)]
#     for i in range(N):
#         for j in range(N):
#             cnt_sum[tmp[i][j]][0] += 1
#             cnt_sum[tmp[i][j]][1] += board[i][j]
    
#     do_continue = False
#     for i in range(nations):
#         if cnt_sum[i][0] > 1:
#             do_continue = True
#             break
    
#     if do_continue is False:
#         break
    
#     avg = [cnt_sum[i][1] // cnt_sum[i][0] for i in range(nations)]
#     for i in range(N):
#         for j in range(N):
#             board[i][j] = avg[tmp[i][j]]
#     loops += 1

# print(loops)

# 시간초과(40분)를 하여 2시간 넘게 생각하며 푼듯. 생각보다 어떻게 효율적으로 처리할지 고민하다가
# 시간이 다 간 케이스... 근데 기껏 풀었는데 시간초과(python3)와 메모리초과(pypy3)가 났음
# BFS, DFS 다 구현 했는데도 초과가 났음...
# https://www.acmicpc.net/problem/16234


# 2. 답지 보고 내 코드 수정해서 다시 풀었는데도... 자꾸 시간 초과가 뜨고 답이 틀리네..?
#    개 삽질의 삽질을 한 끝에 왜 그런지 알아냄...
# 아래의 bfs가 문제였던것!!! 1번에서도 문제였던 것!!!
# (중요) 나는 코드 큐에 넣기 전에 처리해야 하는 부분의 내용이 처음이랑 while 문 안에 똑같이 두번 들어가야 해서
# 간단하게 한다고, queue에 일단 먼저 넣고 뺀 다음에 처리를 했는데.... <- 치명적인 실수!!!
# queue에 넣기 전에 tmp 값을 안바꿔줘 버리면 다음 아이템이 나왔을때 tmp에서 그 자리가 아직 처리가 안되어있어서
# 방문하지 않은 줄 알고 또 방문해버림....! 이것이 문제였던것!!! 매우 중요한 발견!!!
# 정리 : 넣어주기 전에 처리 해야 할지 넣고 나서 뺀 다음에 처리해도 될지를 구분하는게 매우 중요!!!

# 아래 처럼 하면 안됨!!!
def bfs_nakyeon_fail(tmp, i, j, nat):
    global N, L, R
    united = []
    count = 0
    tot_sum = 0
    q = deque([(i, j)])
    while q:
        x, y = q.popleft()
        # 여기서 한꺼번에 처리 했던 것이 문제...!
        tmp[x][y] = nat
        united.append((x, y))
        count += 1
        tot_sum += board[x][y]
        for n in range(4):
            ni = x + di[n]
            nj = y + dj[n]
            if 0 <= ni < N and 0 <= nj < N and tmp[ni][nj] == -1:
                if L <= abs(board[x][y] - board[ni][nj]) <= R:
                    q.append((ni, nj))

    avg = tot_sum // count
    for x, y in united:
        board[x][y] = avg

def bfs_right(tmp, i, j, nat):
    global N, L, R
    united = []
    count = 0
    tot_sum = 0
    q = deque([(i, j)])
    # 이 줄이 포인트!! 큐에 넣기전 반드시 먼저 값을 넣어줘야 함.
    # 매번 if 문으로 이 부분을 체크하기 때문
    tmp[i][j] = nat
    while q:
        x, y = q.popleft()
        united.append((x, y))
        count += 1
        tot_sum += board[x][y]
        for n in range(4):
            ni = x + di[n]
            nj = y + dj[n]
            if 0 <= ni < N and 0 <= nj < N and tmp[ni][nj] == -1:
                if L <= abs(board[x][y] - board[ni][nj]) <= R:
                    # 여기에 한줄 더 추가됨!
                    # 근데 이제 tmp만 여기서 처리하고 나머지는 또 pop 해서 처리하면 코드가 더 깔끔해 지긴 하지만
                    # 헷갈릴 수가 있어서, 코드가 중복되더라도 모든 처리를 다 한 후에, 큐에 넣는다고 생각하는게 더 나을듯
                    tmp[ni][nj] = nat
                    q.append((ni, nj))

    avg = tot_sum // count
    for x, y in united:
        board[x][y] = avg


loops = 0
while True:
    tmp = [[-1] * N for _ in range(N)]
    nations = 0
    for i in range(N):
        for j in range(N):
            if tmp[i][j] == -1:
                bfs_right(tmp, i, j, nations)
                nations += 1

    # 나처럼 일일이 cnt 세서 1보다 큰 놈이 하나라도 있는걸 재는게 아니라 이렇게 심플하게 재는게 좋겠다
    if nations == N * N:
        break
    
    loops += 1

print(loops)
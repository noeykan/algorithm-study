import sys
sys.setrecursionlimit(10**6)

N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def dfs(tmp, i, j, nat):
    global N, L, R
    tmp[i][j] = nat
    for n in range(4):
        ni = i + di[n]
        nj = j + dj[n]
        if 0 <= ni < N and 0 <= nj < N:
            diff = abs(board[i][j] - board[ni][nj])
            if tmp[ni][nj] == -1 and L <= diff <= R:
                dfs(tmp, ni, nj, nat)

loops = 0
while True:
    tmp = [[-1] * N for _ in range(N)]
    nations = 0
    for i in range(N):
        for j in range(N):
            if tmp[i][j] == -1:
                dfs(tmp, i, j, nations)
                nations += 1
    
    cnt_sum = [[0, 0] for _ in range(nations)]
    for i in range(N):
        for j in range(N):
            cnt_sum[tmp[i][j]][0] += 1
            cnt_sum[tmp[i][j]][1] += board[i][j]
    
    do_continue = False
    for i in range(nations):
        if cnt_sum[i][0] > 1:
            do_continue = True
            break
    
    if do_continue is False:
        break
    
    avg = [cnt_sum[i][1] // cnt_sum[i][0] for i in range(nations)]
    for i in range(N):
        for j in range(N):
            board[i][j] = avg[tmp[i][j]]
    loops += 1

print(loops)

from collections import deque

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# BFS
def bfs(r, c):
    q = deque([[r, c]])
    while q:
        i_now, j_now = q.popleft()
        dst = maze[i_now][j_now]
        for n in range(len(di)):
            i = i_now + di[n]
            j = j_now + dj[n]
            if i < 0 or i >= N or j < 0 or j >= M:
                continue
            if maze[i][j] == 0:
                continue
            if maze[i][j] != 1 and maze[i][j] <= dst + 1:
                continue
            maze[i][j] = dst + 1
            q.append([i, j])

bfs(0, 0)
print(maze[N-1][M-1])

# 시간제한(30분) 내에 풀었음
# 1. 답지를 보니 if 문 중 세번째 if 문에서 굳이 저렇게 두 조건 복잡하게 할 필요 없어보임
#    어차피 처음 최소 거리 값을 입력해 버리면 그 뒤에 쓰는 값은 그것보다 크기때문에 고려할 필요 없음
#    따라서 그냥 마지막은 if maze[i][j] == 1: 하면 아래 두줄 실행하는 게 더 나음
# 2. 마지막에 maze[N-1][M-1]을 프린트 하는 것 보다 깔끔하게 bfs 함수 안에 넣어서 return 으로 받는게 더 나은 듯

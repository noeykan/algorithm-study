# 251120

# INPUT
# 15 14
# 00000111100000
# 11111101111110
# 11011101101110
# 11011101100000
# 11011111111111
# 11011111111100
# 11000000011111
# 01111111111111
# 00000000011111
# 01111111111000
# 00011111111000
# 00000001111000
# 11111111110011
# 11100011111111
# 11100011111111

N, M = map(int, input().split())
data = [list(map(int, input())) for _ in range(N)]

di_l = [0, 1, 0, -1]
dj_l = [1, 0, -1, 0]

# 1. DFS, 재귀
# def dfs(data, i, j, start):
#     if i >= 0 and i < N and j >= 0 and j < M and data[i][j] == 0:
#         data[i][j] = start
#         for di, dj in zip(di_l, dj_l):
#             dfs(data, i + di, j + dj, start)
#     else:
#         return

# start = 2
# for i in range(N):
#     for j in range(M):
#         if data[i][j] == 0:
#             dfs(data, i, j, start)
#             start += 1
# print(start - 2)

# 26m
# 1) dfs 쓰기 전에 if 문을 썼는데, dfs 안에도 if 문 있어서 이 중복을 피하려면 return 값을 True/False로 만들면 됨
# 2) 굳이 map에 글씨 쓸 때 2부터 썼는데 사실 그냥 채울때마다 1로 하면 될뻔했네. dfs 함수에 start 가 안들어가도 됨


# 2. 위 바탕으로 다시 푼 풀이 (DFS, 재귀)
# def dfs(i, j):
#     if i >= 0 and i < N and j >= 0 and j < M and data[i][j] == 0:
#         data[i][j] = 1
#         for di, dj in zip(di_l, dj_l):
#             dfs(i + di, j + dj)
#         return True
#     else:
#         return False

# cnt = 0
# for i in range(N):
#     for j in range(M):
#         if dfs(i, j):
#             cnt += 1
# print(cnt)


# 3. DFS, 반복문. 풀다가 어려워서 AI도움받음
def dfs_iter(i, j):
    if data[i][j] == 0:
        stack = [(i, j)]
        # 중요!!!! stack에 데이터 넣기 전에 미리 방문 처리 해야 함. 나중에 pop에서 방문처리 하면 스택에 좌표가 중복해서 들어감!!!!
        # DFS 재귀함수는 그렇게 안해도 되는데 stack 쓸 때는 이렇게 해야함.
        data[i][j] = 1
        while stack:
            ci, cj = stack.pop()
            # reversed 하는 이유 : stack 특성상 내가 넣은 방향(우,하,좌,상)과 다르게 거꾸로 호출되니까 넣은 방향과 동일하게 호출하기 위해
            # 답에는 지장 없지만 그래도 확실하게 하고싶음
            for k in reversed(range(4)):
                ni, nj = ci + di_l[k], cj + dj_l[k]
                if 0 <= ni < N and 0 <= nj < M and data[ni][nj] == 0:
                    data[ni][nj] = 1
                    stack.append((ni, nj))
        return True
    else:
        return False

cnt = 0
for i in range(N):
    for j in range(M):
        if dfs_iter(i, j):
            cnt += 1
print(cnt)

# 4. BFS는 그냥 3번 코드에서 stack을 queue로만 바꿔주면 끝

# https://www.acmicpc.net/problem/11123
# 양 한마리... 양 두마리...

import sys
input = sys.stdin.readline

t = int(input())

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# 1. DFS
# sys.setrecursionlimit(10**6)
#
# def dfs(grid, h, w, i, j):
#     grid[i][j] = 2
#     for x in range(4):
#         ni = i + di[x]
#         nj = j + dj[x]
#         if 0 <= ni < h and 0 <= nj < w and grid[ni][nj] == 1:
#             dfs(grid, h, w, ni, nj)
#
# for _ in range(t):
#     h, w = map(int, input().split())
#     grid = [[1 if x == '#' else 0 for x in input().rstrip()] for _ in range(h)]
#     cnt = 0
#     for i in range(h):
#         for j in range(w):
#             if grid[i][j] == 1:
#                 dfs(grid, h, w, i, j)
#                 cnt += 1
#     print(cnt)

# 2. BFS
from collections import deque

def bfs(grid, i, j):
    if grid[i][j] != 1:
        return False
    h = len(grid)
    w = len(grid[0])
    grid[i][j] = 2
    q = deque([])
    q.append((i, j))
    while q:
        ci, cj = q.popleft()
        for x in range(4):
            ni = ci + di[x]
            nj = cj + dj[x]
            if 0 <= ni < h and 0 <= nj < w and grid[ni][nj] == 1:
                grid[ni][nj] = 2
                q.append((ni, nj))
    return True

for _ in range(t):
    h, w = map(int, input().split())
    grid = [[1 if x == '#' else 0 for x in input().rstrip()] for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if bfs(grid, i, j):
                cnt += 1
    print(cnt)
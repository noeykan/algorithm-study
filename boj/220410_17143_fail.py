# https://www.acmicpc.net/problem/17143
# 낚시왕

import sys
input = sys.stdin.readline

# 0 위 / 1 아래 / 2 오른 / 3 왼
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

r, c, m = map(int, input().split())
shark = [[] for _ in range(m)]
grid = [[None] * c for j in range(r)]
for i in range(m):
    # 0,1 상어 위치(r,c) / 2 속력 / 3 이동방향 / 4 크기
    row, col, vel, dr, wg = list(map(int, input().split()))
    # 기준을 0으로 만듦
    shark[i] = [row - 1, col - 1, vel, dr - 1, wg]
    grid[shark[i][0]][shark[i][1]] = i

shark_weight = 0
for col in range(c):
    # 상어 잡기
    for row in range(r):
        # 가장 가까운 상어 한마리 잡음
        caught = grid[row][col]
        if caught is not None:
            shark_weight += shark[caught][4]
            del shark[caught]
            break

    # 상어 이동
    tmp = [[None] * c for j in range(r)]
    for i in range(m):
        sr, sc, v, d, w = shark[i]
        # gg...
        nr = sr + dr[d] * v
        nc = sc + dc[d] * v

    grid = tmp

print(shark_weight)

# 결국 상어 이동하는 부분(방향전환)이 핵심이고 이거 때문에 몇시간을 날렸음...
# 0  1  2  3                   1을빼줌
# ->            0      0 + 0   -1
#    ->         1      0 + 1    0 : 몫 0 나머지 0
#       ->     [2]     0 + 2    1 : 몫 0 나머지 1
#          ->   3      0 + 3    2 : 몫 0 나머지 2
#       <-      4(2)   3 - 1    3 : 몫 1 나머지 0
#    <-       [[5(1)]] 3 - 2    4 : 몫 1 나머지 1
# <-            6(0)   3 - 3    5 : 몫 1 나머지 2
#    ->         7(1)   0 + 1    6 : 몫 2 나머지 0
#       ->     [8(2)]  0 + 2    7 : 몫 2 나머지 1
#          ->   9(3)
#       <-      10(2)
#    <-       [[11(1)]]
# <-            12(0)
#

# https://www.acmicpc.net/problem/17143
# 낚시왕

import sys
input = sys.stdin.readline

# 1 위 / 2 아래 / 3 오른 / 4 왼
di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, 1, -1]

r, c, m = map(int, input().split())
shark = [[] for _ in range(m + 1)]
grid = [[[] for _ in range(c + 1)] for j in range(r + 1)]
for i in range(1, m + 1):
    # 0,1 상어 위치(r,c) / 2 속력 / 3 이동방향 / 4 크기 / 5 생존여부(0:죽음 1:살아있음)
    shark[i] = list(map(int, input().split())) + [1]
    grid[shark[i][0]][shark[i][1]].append(i)

shark_weight = 0
for col in range(1, c + 1):
    # 상어 잡기
    for row in range(1, r + 1):
        # 가장 가까운 상어 한마리 잡음
        if len(grid[row][col]) == 1:
            caught = grid[row][col][0]
            grid[row][col].remove(caught)
            shark[caught][5] = 0
            shark_weight += shark[caught][4]
            break
        elif len(grid[row][col]) > 1:
            print(f"Error. 상어가 grid[{row}][{col}]에 2마리 이상 있음")
            exit(0)

    # 상어 이동
    for i in range(1, m + 1):
        # 살아있을 시
        if shark[i][5] == 1:
            grid[shark[i][0]][shark[i][1]].remove(i)
            # 1  2  3  4
            # ->            1
            #    ->         2
            #       ->     [3] -> 속도가 1000이면
            #          ->
            #       <-
            #    <-
            # <-
            #    ->         8 위치 2
            #       ->     [9]
            #
            # 상어 이동.. 이부분 어떻게..?
            #
            grid[shark[i][0]][shark[i][1]].append(i)

    # 상어 중복 처리
    for row in range(1, r + 1):
        for col in range(1, c + 1):
            if len(grid[row][col]) > 1:
                # 몸무게 순으로 내림차순 정렬
                grid[row][col].sort(key=lambda i: shark[i][4], reverse=True)
                for i in range(1, len(grid[row][col])):
                    dead = grid[row][col][i]
                    grid[row][col].remove(dead)
                    shark[dead][5] = 0

print(shark_weight)
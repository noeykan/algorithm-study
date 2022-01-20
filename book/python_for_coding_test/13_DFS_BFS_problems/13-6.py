from itertools import combinations

N = int(input())
board = [list(input().split()) for _ in range(N)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def spy(i, j, i_diff, j_diff):
    if i < 0 or i >= N or j < 0 or j >= N or board[i][j] == 'T' or board[i][j] == 'O':
        return False
    if board[i][j] == 'S':
        return True
    return spy(i + i_diff, j + j_diff, i_diff, j_diff)

empty = []
teacher = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 'X':
            empty.append((i, j))
        elif board[i][j] == 'T':
            teacher.append((i, j))

result = False
for empty_selected in combinations(empty, 3):
    for i, j in empty_selected:
        board[i][j] = 'O'

    can_avoid = True
    for i, j in teacher:
        for n in range(4):
            ni = i + di[n]
            nj = j + dj[n]
            if spy(ni, nj, di[n], dj[n]):
                can_avoid &= False

    for i, j in empty_selected:
        board[i][j] = 'X'

    if can_avoid:
        result = True
        break

if result:
    print("YES")
else:
    print("NO")

# 50분에 품 (제한시간 60분)
# 중간에 실수로 삽질 몇번 했으나 다행히 시간이 넉넉하게 주어져서 품
# https://www.acmicpc.net/problem/18428
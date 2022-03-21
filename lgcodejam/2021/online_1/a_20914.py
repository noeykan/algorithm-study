# A. QWERTY 자판

# 내 풀이
import copy
from collections import deque

keyboard = [list('QWERTYUIOP'), list('ASDFGHJKL0'), list('ZXCVBNM000')]
w = len(keyboard[0])
h = len(keyboard)
di = [0, -1, -1, 0, 1, 1]
dj = [-1, 0, 1, 1, 0, -1]
board = [[0]*w for _ in range(h)]

def index_2d(arr, x):
    for i, a in enumerate(arr):
        if x in a:
            return i, a.index(x)

def bfs(start, end):
    b = copy.deepcopy(board)
    q = deque([start])
    while q:
        x = q.popleft()
        i, j = index_2d(keyboard, x)
        if x == end:
            return b[i][j]
        for a in range(6):
            ni = i + di[a]
            nj = j + dj[a]
            if 0 <= ni < h and 0 <= nj < w and keyboard[ni][nj] != '0' and b[ni][nj] == 0:
                b[ni][nj] = b[i][j] + 2
                q.append(keyboard[ni][nj])

n = int(input())
for _ in range(n):
    word = input()
    total_time = 0
    for i in range(len(word) - 1):
        # 누르고 이동
        total_time += (1 + bfs(word[i], word[i + 1]))
    # 마지막 버튼 누름
    total_time += 1
    print(total_time)

# 한시간 안걸리게 풀었는데 해설을 보니 훨씬 더 쉽게 풀었네 ;;;
# 1) 나는 BFS로 풀었는데 답지는 거리계산을 논리적으로 아주 쉽게 풀었음...
#    대체 이걸 어떻게 생각할 수 있는지...ㅎㅎ;;
# 2) 나는 keyboard 문자를 position으로 바꾸는거를 이중배열에서 일일이 매번 find로 찾아서 search 하는데 시간을 계속 썼는데
#    답지는 아예 dict()로 만들어서 바로 1:1 매핑으로 만들어 버림. 이럴때 dict쓰면 편하구나! 알아두자!
# 3) 두 수 모두 음수거나 두 수 모두 양수일 때 답지는 XOR(^) 한 값이 >= 0 이면 이라고 조건을 걸었는데 참신하고 간단하다
#    최상위 부호비트가 모두 0이거나 모두 1일때는 XOR 하면 부호비트는 0이 나오므로 양수니까 >= 0 이고,
#    최상위 부호비트가 하나는 0이고 하나는 1일때는 XOR 하면 부호비트는 1이 나오므로 음수니까 < 인 것이다...! 알아두자!
# 4) 답을 구할때도 나처럼 누르고 이동하고 마지막 버튼을 또 추가로 해주지 않아도
#    문자열 길이를 처음에 초기값으로 세팅하고, 이동할때마다 2씩만 더 더해주면 더 깔끔하다...
# https://codejam.lge.com/problem/20914

# 해설 풀이
# http://collab.lge.com/main/display/Expert/LGE+Code+Jam+2021+-+Problem+A

# import sys
#
# keys = ["QWERTYUIOP",
#         "ASDFGHJKL",
#         "ZXCVBNM"]
#
# key_pos = dict()
# for i in range(len(keys)):
#     line = keys[i]
#     for j in range(len(line)):
#         key = line[j]
#         key_pos[key] = (i, j)
#
#
# def solve(case):
#     s = sys.stdin.readline().strip()
#
#     result = len(s)
#
#     cur = s[0]
#     cur_r, cur_c = key_pos[cur]
#
#     for i in range(1, len(s)):
#         next = s[i]
#         next_r, next_c = key_pos[next]
#
#         diff_r, diff_c = next_r - cur_r, next_c - cur_c
#
#         # if (diff_r >= 0 and diff_c >= 0) or (diff_r < 0 and diff_c < 0):
#         # if diff_r ^ diff_c >= 0:
#         #     result += abs(diff_r + diff_c) * 2
#         # else:
#         #     result += max(abs(diff_r), abs(diff_c)) * 2
#         result += max(abs(diff_r + diff_c), abs(diff_r), abs(diff_c)) * 2
#
#         cur_r, cur_c = next_r, next_c
#
#     print(result)
#
#
# if __name__ == "__main__":
#     t = int(sys.stdin.readline())
#     for i in range(t):
#         solve(i)
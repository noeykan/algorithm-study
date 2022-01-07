from collections import deque

N = int(input())
K = int(input())
apples = [list(map(int, input().split())) for _ in range(K)]
L = int(input())
snake_moves = deque(list(input().split()) for _ in range(L))
for m in snake_moves:
    m[0] = int(m[0])

step = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 동남서북
turn = 0

snake = deque([[1, 1]]) # 오른쪽이 머리
sec = 0
while True:
    head = snake[-1]
    if len(snake_moves) > 0 and snake_moves[0][0] == sec:
        turn_direction = snake_moves.popleft()[1]
        turn += 1 if turn_direction == 'D' else -1
        turn = turn % len(step)
    sec += 1
    next_head = [head[0] + step[turn][0], head[1] + step[turn][1]]
    snake.append(next_head)
    if next_head in apples:
        apples.remove(next_head)
    elif snake.count(next_head) > 1 or next_head[0] < 1 or next_head[0] > N or next_head[1] < 1 or next_head[1] > N:
        break
    else:
        snake.popleft()

    # # 디버깅용 맵 print
    # print(f'{sec} sec')
    # for i in range(1, N+1):
    #     for j in range(1, N+1):
    #         if [i, j] in apples:
    #             print('A', end='')
    #         elif [i, j] in snake:
    #             print('O', end='')
    #         else:
    #             print('E', end='')
    #     print('')
    # print('\n')

print(sec)

# 시간초과(40분)하여 한 2시간은 푼 것 같다.. 문제에 애매한 표현이 있어서 삽질하고;; 백준 게시판 질문에서 찾아 보느라 고생했다.
# 가장 크게 삽질 한 것은, 좌표를 (0,0)이 시작이라고 생각 한 것... 나중에 알고보니 (1,1) 부터 시작이었더라..;
# 백준 게시판에서 찾아보고 안 것은, 나는 머리가 늘어나고 꼬리가 작아지면 머리가 꼬리에 안닿는다고 생각했는데 닿는 거였더라.. 표현 애매함

# 백준 아래에서 채점 했을 시에 모두 정답 확인
# https://www.acmicpc.net/problem/3190

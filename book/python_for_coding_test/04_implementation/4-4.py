N, M = map(int, input().split())
i, j, direction = map(int, input().split())
g_map = []
for row in range(N):
    g_map.append(list(map(int, input().split())))

# g_map에서 2는 가본 곳으로 가정하고 현재 위치를 2로 세팅
g_map[i][j] = 2
cnt = 1

# 북동남서
i_steps = [-1, 0, 1, 0]
j_steps = [0, 1, 0, -1]

cnt_visited = 0
while True:
    # 반시계 방향으로 계속 회전하므로, steps의 idx는 계속 -1로 진행되어야 맞음
    dir_next = (direction - 1) % 4
    i_next = i + i_steps[dir_next]
    j_next = j + j_steps[dir_next]

    if g_map[i_next][j_next] == 0:  # 가보지 않은 칸
        direction = dir_next
        i = i_next
        j = j_next
        g_map[i][j] = 2
        cnt += 1
        cnt_visited = 0
    elif g_map[i_next][j_next] == 2 or g_map[i_next][j_next] == 1:  # 가본 칸 or 바다
        if cnt_visited == 4:    # 누적으로 4번 다 막혔을 시
            dir_next = (direction - 2) % 4  # 방향을 유지한채 뒤로 한칸
            i_next = i + i_steps[dir_next]
            j_next = j + j_steps[dir_next]
            if g_map[i_next][j_next] == 1:  # 뒤로 가려는데 바다인 칸 만남
                break
            else:
                i = i_next
                j = j_next
                cnt_visited = 0
                continue
        direction = dir_next
        cnt_visited += 1

print(cnt)

# 시간 초과.. 푸는 데 1시간 반은 걸린 듯 함
# 입력 예시 하나는 맞았는데, 과연 다른 corner case가 없을지..? 정답 코드 보면서 확인 해 봐야 겠음
# 251120

N, M = map(int, input().split())
i, j, d = map(int, input().split())

map_ = [list(map(int, input().split())) for _ in range(N)]

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

map_[i][j] = 2
cnt_visit = 1
cnt_rotate = 0

while True:
    # 왼쪽회전
    d = ((d + 4) - 1) % 4
    cnt_rotate += 1

    ni = i + di[d]
    nj = j + dj[d]
    if map_[ni][nj] == 0:
        i = ni
        j = nj
        map_[ni][nj] = 2 # 가본 칸
        cnt_visit += 1
        cnt_rotate = 0
    else:
        if cnt_rotate == 4:
            # 한칸뒤로
            nd = ((d + 4) - 2) % 4
            ni = i + di[nd]
            nj = j + dj[nd]
            if map_[ni][nj] == 1:
                break
            else:
                i = ni
                j = nj
                cnt_rotate = 0

print(cnt_visit)

# 38m


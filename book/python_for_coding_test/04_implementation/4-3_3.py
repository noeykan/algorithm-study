# 251120

in_str = input()
# ord 까먹어서 결국 정답 봄;; 이거 고민만 5분 한듯
x = ord(in_str[0]) - ord('a') + 1
y = int(in_str[1])

dx_list = [2, 2, 1, -1, -2, -2, -1, 1]
dy_list = [-1, 1, 2, 2, 1, -1, -2, -2]

cnt = 0
for dx, dy in zip(dx_list, dy_list):
    nx = x + dx
    ny = y + dy
    if nx > 0 and ny > 0 and nx <= 8 and ny <= 8:
        cnt += 1

print(cnt)

# 16m
# t:O(1), s:O(1)
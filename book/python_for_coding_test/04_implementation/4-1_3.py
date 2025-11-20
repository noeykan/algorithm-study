# 251120

N = int(input())
data = list(input().split())

cur = [1, 1]
for d in data:
    if d == 'L':
        new_cur = cur[1] - 1
        cur[1] = new_cur if new_cur > 0 else cur[1]
    elif d == 'R':
        new_cur = cur[1] + 1
        cur[1] = new_cur if new_cur <= 5 else cur[1]
    elif d == 'U':
        new_cur = cur[0] - 1
        cur[0] = new_cur if new_cur > 0 else cur[0]
    elif d == 'D':
        new_cur = cur[0] + 1
        cur[0] = new_cur if new_cur <= 5 else cur[0]

print(cur[0], cur[1])

# 12m
# 답지 처럼 풀면 더 일반화시키면서 깔끔하게 풀 수 있을듯

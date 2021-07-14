in_loc = input()

loc = [int(in_loc[1]), int(ord(in_loc[0])-ord('a')+1)]
di = [-2, -1, 1, 2, 2, 1, -1, -2]
dj = [-1, -2, -2, -1, 1, 2, 2, 1]

cnt = 0
for n in range(8):
    ni = loc[0] + di[n]
    nj = loc[1] + dj[n]
    if 1 <= ni <= 8 and 1 <= nj <= 8:
        cnt += 1

print(cnt)

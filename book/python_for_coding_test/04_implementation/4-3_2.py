loc_in = input()
# (행, 열) 순으로 바꾸기
loc = [int(loc_in[1]), ord(loc_in[0])-ord('a')+1]

di = [2, 2, -1, 1, -2, -2, -1, 1]
dj = [-1, 1, 2, 2, -1, 1, -2, -2]

cnt = 0
for idx in range(len(di)):
    i = loc[0] + di[idx]
    j = loc[1] + dj[idx]
    if 1 <= i <= 8 and 1 <= j <= 8:
        cnt += 1
print(cnt)

# 13분
# 답지를 보니 di, dj 이렇게 분리하는 것 말고도 튜플 리스트 형태로 쓰기도 함. 참고.
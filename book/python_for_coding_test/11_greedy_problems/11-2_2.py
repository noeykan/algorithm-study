# 251203

# 왼쪽 (x or +) 오른쪽
# 왼쪽이나 오른쪽 모두 0이거나 1이면 더하기, 나머지는 곱하기

#data = [int(s) for s in input()]
data = list(map(int, input()))

ans = data[0]
for i in range(1, len(data)):
    if ans == 0 or ans == 1 or data[i] == 0 or data[i] == 1:
        ans += data[i]
    else:
        ans *= data[i]
print(ans)

# 15m
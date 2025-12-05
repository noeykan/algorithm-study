# 251203

data = input()

cnt = 1
prev_s = data[0]

for i in range(1, len(data)):
    if data[i] != prev_s:
        cnt += 1
        prev_s = data[i]

print(cnt // 2)

# 10m
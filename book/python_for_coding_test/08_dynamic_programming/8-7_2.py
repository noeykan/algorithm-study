#251123

n = int(input())

d = [0] * 1001
d[1] = 1
d[2] = 3

for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2] * 2

print(d[n] % 796796)

# 20m : 20분동안 개 헤맸는데 별거 아니었네 후;;
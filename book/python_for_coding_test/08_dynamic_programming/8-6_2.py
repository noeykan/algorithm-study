#251123

n = int(input())
data = list(map(int, input().split()))

a = [0] * 100
a[0] = data[0]
a[1] = data[1]

for i in range(2, n):
    a[i] = max(a[i - 1], a[i - 2] + data[i])

print(a[n - 1])

# 9m
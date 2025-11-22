#251122

N, K = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

cnt = 0
for i in range(K):
    cnt += max(a[i], b[i])

for i in range(K, N):
    cnt += a[i]

print(cnt)
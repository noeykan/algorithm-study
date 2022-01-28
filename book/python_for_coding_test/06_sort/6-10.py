# 위에서 아래로
N = int(input())
data = [input() for _ in range(N)]
print(*sorted(data, reverse=True), sep=' ')
# 31. 금광

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    data_1d = list(map(int, input().split()))
    data = []
    for i in range(N):
        data.append(data_1d[M*i:M*(i+1)])

    d = [[0] * M for _ in range(N)]
    for i in range(N):
        d[i][0] = data[i][0]
    for j in range(1, M):
        for i in range(N):
            if i == 0:
                d[i][j] = data[i][j] + max(d[i][j - 1], d[i + 1][j - 1])
            elif i == N - 1:
                d[i][j] = data[i][j] + max(d[i - 1][j - 1], d[i][j - 1])
            else:
                d[i][j] = data[i][j] + max(d[i - 1][j - 1], d[i][j - 1], d[i + 1][j - 1])
    print(max([row[M-1] for row in d]))
    # 아래 처럼 하다 답이 안나와서 삽질 했는데 아래는 Numpy에서만 쓸 수 있는 것... -_- 헷갈리지 말자
    # print(max(d[:][M-1]))

# 제한시간(30분) 내에 풂
# 위에 적었듯 numpy에서 쓰는 문법 쓰면 내가 생각하는 동작을 하지 않음 주의
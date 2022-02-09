# 3. 개미 전사

N = int(input())
data = list(map(int, input().split()))

# 첫번째 풀이
# d[n][0]: n번째를 포함 안할 때 최대 식량
# d[n][1]: n번째를 포함 할 때 최대 식량
# d = [[0]*2 for _ in range(N)]

# d[0][1] = data[0]
# for i in range(1, N):
#     d[i][0] = d[i-1][1]
#     d[i][1] = d[i-2][1] + data[i]

# print(max(d[N-1][0], d[N-1][1]))

# 답 보고 다시 풀어보기
# d[n] : n번째까지 중 최대 식량
d = [0] * N
d[0] = data[0]
for i in range(1, N):
    d[i] = max(d[i - 2] + data[i], d[i - 1])
print(d[N-1])

# 문제는 풀었으나 너무 어렵게 생각했네 -_- 이중배열 필요없음... 오랜만에 풀어서 그런가 감떨어짐

# 36. 편집거리

str1 = input()
str2 = input()

N = len(str1) + 1
M = len(str2) + 1
dp = [[0] * M for _ in range(N)]

for i in range(N):
    dp[i][0] = i
for j in range(M):
    dp[0][j] = j

for i in range(1, N):
    for j in range(1, M):
        if str1[i - 1] == str2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

print(dp[N - 1][M - 1])

# 제한시간(30분) 까마득히 넘게 생각했는데 결국 못풀어서 답지 봄...
# 와 어떻게 이런 생각을 하지..? 답지 봐도 이해 안돼서 한참 생각하다가 겨우 이해함;;

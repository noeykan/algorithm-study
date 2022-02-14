# 34. 병사 배치하기

N = int(input())
data = list(map(int, input().split()))

# dp[n] = n번째 병사를 포함한 최대 병사의 수
dp = [0] * N
dp[0] = 1

for i in range(1, N):
    max_cnt = 1
    for j in range(i - 1, -1, -1):
        if data[i] < data[j]:
            max_cnt = max(max_cnt, dp[j] + 1)
    dp[i] = max_cnt
    
print(N - max(dp))

# 제한시간(40분) 내에 풀었음
# 위에서 dp를 1로 초기화 했으면 코드가 훨씬 간단 해졌을 것.
# max_cnt를 안써도 되고, 그냥 그 대신 dp[i]로 했으면 됐을 듯.
# https://www.acmicpc.net/problem/18353
